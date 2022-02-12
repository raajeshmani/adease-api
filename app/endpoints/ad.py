from flask import Blueprint, jsonify, request
from ..task import generate_random_ads_task, fetch_metadata_task
from ..helpers import is_valid_youtube_url, is_ad_data_valid
from .. import db
import datetime, json, traceback
from bson.json_util import loads, dumps
import time

ad = Blueprint(name="ad", import_name=__name__)

def create_ad(data):
    valid_data = []

    for ad_data in data:
        if is_ad_data_valid:
            datetime_val = str(datetime.datetime.now())
            print(ad_data)
            metadata = fetch_metadata_task(ad_data['destination_url'])

            ad_data['metadata'] = metadata
            ad_data['content_url'] = metadata['thumbnail_url']
            ad_data['created_at'] = datetime_val
            ad_data['updated_at'] = datetime_val
            if 'headline' not in ad_data.keys() or ad_data['headline'] == '':
                headline = metadata['title']
            if 'primary_text' not in ad_data.keys() or ad_data['primary_text'] == '':
                ad_data['primary_text'] = metadata['author_name'] + ' ' + metadata['author_url']

            valid_data.append(ad_data)
    return db.ad.insert_many(valid_data)

def get_ad():
    ads = db.ad.find()
    return list(ads)

def update_ad(name, replacement):
    replacement['updated_at'] = str(datetime.datetime.now())
    return db.ad.update_one({'name': name}, {'$set': replacement})
    # return db.ad.replace_one({'name': name}, replacement)

def delete_ad():
    return db.ad.drop()


# CREATE
@ad.route('/add', methods=['POST'])
def add():
    try:
        data = request.args.get('data')

        inserted_ads = create_ad(loads(data))
        print("DEBUG: Inserted Ads",inserted_ads.acknowledged)
        return jsonify({"message": "Inserted into Collection Ad","result": inserted_ads.acknowledged})
    except Exception as e:
        print("Exception =>", e)
        traceback.print_exc()
        return

# READ
@ad.route('/', methods=['GET'])
def index():
    ads = loads(dumps(get_ad()))
    for ad in ads:
        del ad['_id']

    print("DEBUG: Retrieved Ads - count ", len(ads))

    output = {"message": "Retrieve all Ads", "result": ads, "count": len(ads)}
    # Adding manual sleep to visualize beautiful loading
    # time.sleep(2)
    return jsonify(output)

# UPDATE
@ad.route('/update', methods=['POST', 'PUT'])
def update():
    try:
        replace_data = request.args.get('replace')
        name = request.args.get('name')
        replaced_ads = update_ad(name, loads(replace_data))
        print("DEBUG: Replaced Ads",replaced_ads.acknowledged)
        return jsonify({"message": "Replaced into Collection Ad","result": replaced_ads.acknowledged})
    except Exception as e:
        print("Exception =>", e)
        traceback.print_exc()
        return


# DELETE
@ad.route('/delete', methods=['DELETE'])
def delete():
    deleted_ads = False
    try:
        delete_ad()
        deleted_ads = True
    except Exception as e:
        print("Exception =>", e)
        traceback.print_exc()
    return jsonify({"message": "Deleted a Collection Ad","result": deleted_ads})


# RANDOM generator
@ad.route('/random', methods=['POST'])
def random():
    try:
        inserted_ads = generate_random_ads_task(int(request.args.get('size')))
        print("DEBUG: Randomly Populated Ads",inserted_ads.acknowledged)
        return jsonify({"message": "Randomly Populated Ads","result": inserted_ads.acknowledged})
    except Exception as e:
        print("Exception =>", e)
        traceback.print_exc()
        return
