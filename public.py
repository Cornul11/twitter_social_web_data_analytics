import tweepy
import time
import sys
import os
import json

from dotenv import load_dotenv

config = load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

data = []

# max_time 120 times 60 seconds = 10 minutes
max_time = time.time() + 60 * 10


class StdOutListener(tweepy.Stream):
    def on_status(self, status):
        print(status)

    def on_data(self, raw_data):
        if time.time() < max_time:
            data.append(json.loads(raw_data.decode("utf-8")))
        else:
            with open('public.json', 'w') as f:
                json.dump(data, f)
            sys.exit(0)


# file used to sample 10 minutes of the public twitter stream
if __name__ == '__main__':
    stream = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.sample()
