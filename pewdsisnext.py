from twython import Twython
from twitter import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
from youtube import (
    api_key
)
from messages import generate_message

import requests
import time
import schedule


PEWDIEPIE_CHANNEL_ID = "UC-lHJZR3Gqxm24_Vd_AJ5Yw"
JAKE_PAUL_CHANNEL_ID = "UCcgVECVN4OKV6DH1jLkqmcA"

last_tweeted_message_index = 0
day = 0


def get_subcount(ID):
    res = requests.get(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + ID + "&key=" + api_key)
    data = res.json()
    subcount = data["items"][0]["statistics"]["subscriberCount"]

    return subcount


def intWithCommas(x):
    if type(x) not in [type(0), type(0)]:
        raise TypeError("Parameter must be an integer.")
    if x < 0:
        return '-' + intWithCommas(-x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)


def run():
    global last_tweeted_message_index

    pewdiepie_subcount = get_subcount(PEWDIEPIE_CHANNEL_ID)
    jake_paul_subcount = get_subcount(JAKE_PAUL_CHANNEL_ID)
    diff = int(pewdiepie_subcount) - int(jake_paul_subcount)

    tw = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    diff = intWithCommas(diff)
    print(diff)
    message, index = generate_message(diff, last_tweeted_message_index, day)
    last_tweeted_message_index = index
    tw.update_status(status=message)
    print(f"Tweeted: {message}")


schedule.every().day.at("16:35").do(run)

while True:
    schedule.run_pending()
    time.sleep(59)
