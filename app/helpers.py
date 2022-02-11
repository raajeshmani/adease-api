import random, string, datetime
from urllib.parse import urlparse

# Validates both original url and shortened url
# https://www.youtube.com/watch?v=O3-Jiejdr7E
# https://youtu.be/O3-Jiejdr7E
def is_valid_youtube_url(url):
    parsed = urlparse(url)
    if (parsed.scheme=='https' and parsed.netloc=='www.youtube.com' and parsed.path=='/watch' and parsed.query):
        return True
    elif (parsed.scheme=='https' and parsed.netloc=='youtu.be' and parsed.path):
        return True
    return False

# Validates imgur url
# https://imgur.com/gallery/YZ1yC5a
def is_valid_imgur_url(url):
    parsed = urlparse(url)
    if (parsed.scheme=='https' and parsed.netloc=='imgur.com' and parsed.path.find('/gallery/') != -1):
        return True
    return False


'''
Sample Valid data
[{
    "destination_url": "https://imgur.com/gallery/YZ1yC5a",
    "headline": "ikaqvdgtuhlhynbtgztf Ad",
    "name": "Ad no 02",
    "primary_text": "yvxjvmjwkctbgzkjxnogrnrxzeepxzetttzxgotkvsjhgldbcjbrherlxvehuvxiztfslqeatveieqbqpcgxxngqajikinrlwbtc",
    "type": "IMAGE_AD"
},
{
    "destination_url": "https://www.youtube.com/watch?v=O3-Jiejdr7E",
    "headline": "ikaqvdgtuhlhynbtgztf Ad",
    "name": "Ad no 52",
    "primary_text": "yvxjvmjwkctbgzkjxnogrnrxzeepxzetttzxgotkvsjhgldbcjbrherlxvehuvxiztfslqeatveieqbqpcgxxngqajikinrlwbtc",
    "type": "IMAGE_AD"
}]
'''
def is_ad_data_valid(data):
    if (
        data['name']
        and (data['primary_text'] and len(data['primary_text']) <= 120)
        and (data['headline'] and len(data['headline']) <= 30)
        and data['type']
    ):
        url_type = data['type']
        if (
            url_type == 'IMAGE_AD'
            and (data['destination_url'] and is_valid_imgur_url(data['destination_url']))
            ):
            return True
        if (
            url_type == 'VIDEO_AD'
            and (data['destination_url'] and is_valid_youtube_url(data['destination_url']))
            ):
            return True
        return False
    return False
