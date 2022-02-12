from . import db, celery
import datetime, requests, random, string

# from flask import current_app
# app = current_app._get_current_object()

@celery.task(name='app.tasks.generate_random_ads')
def generate_random_ads_task(size):
    generated_ads = []
    for _ in range(size):
        ad_type = random.choice(['IMAGE_AD','VIDEO_AD'])
        destination_url = ''
        if ad_type == 'IMAGE_AD':
            destination_url = "https://imgur.com/gallery/" + str(''.join(random.choices(string.ascii_letters + string.digits, k = 7)))
        elif ad_type == 'VIDEO_AD':
            destination_url = "https://www.youtube.com/watch?v=" + str(''.join(random.choices(string.ascii_letters + string.digits, k = 11)))

        # Queue metadata fetvhing
        metadata = fetch_metadata_task(destination_url)
        if metadata['title'] == '':
            headline = str(''.join(random.choices(string.ascii_lowercase, k = 20))) + ' Ad'
        else:
            headline = metadata['title']
        generated_ads.append({
                "name": "Ad no " + str(''.join(random.choices(string.digits, k = 2))),
                "type": ad_type,
                "content_url" : metadata['thumbnail_url'],
                "headline" : headline,
                "primary_text" : str(''.join(random.choices(string.ascii_lowercase, k = 100))),
                "destination_url" : destination_url,
                "metadata" : metadata,
                "created_at" : str(datetime.datetime.now()),
                "updated_at" : str(datetime.datetime.now())
            })
    return db.ad.insert_many(generated_ads)


@celery.task(name='app.tasks.fetch_metadata')
def fetch_metadata_task(url):
    #! TODO - Find Imgur metadata fetch url
    # https://api.imgur.com/post/v1/posts/kkBc2Di/meta?client_id=546c25a59c58ad7&include=post,user,accolades
    req_metadata = requests.get("https://youtube.com/oembed?url=" + url + "&format=json")
    if req_metadata.status_code == 200:
        metadata = req_metadata.json()
    else:
        metadata = { 'thumbnail_url': '', 'title': '', 'author_name': '', 'author_url': ''}
    return metadata


