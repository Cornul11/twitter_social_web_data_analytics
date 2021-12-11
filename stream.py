import tweepy
import time
import json
import sys
import os

from dotenv import load_dotenv

config = load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


class TwitterStreamListener(tweepy.Stream):
    def __init__(self, duration, filename):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        self.data = []
        self.filename = filename
        self.max_time = time.time() + duration
        print("Started collecting tweets for " + str(duration) + " seconds into file " + filename)

    def on_status(self, status):
        print(status)

    def on_data(self, raw_data):
        if time.time() < self.max_time:
            self.data.append(json.loads(raw_data.decode("utf-8")))
        else:
            with open(self.filename, 'w') as f:
                json.dump(self.data, f)
            sys.exit(0)
