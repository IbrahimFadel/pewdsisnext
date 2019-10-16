from twython import Twython
from twitter import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

tw = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = "Hello world!"
tw.update_status(status=message)
print("Tweeted: %s" % message)
