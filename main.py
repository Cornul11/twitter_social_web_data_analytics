import tweepy
import time
import sys
import os

from dotenv import load_dotenv

config = load_dotenv()

consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

data = []

# max_time 10 times 60 seconds
max_time = time.time() + 60 * 10


class StdOutListener(tweepy.Stream):
    def on_status(self, status):
        print(status)

    def on_data(self, raw_data):
        if time.time() < max_time:
            data.append(raw_data)
        else:
            with open('dump.log', 'w') as f:
                for item in data:
                    f.write("%s\n" % item)
            sys.exit(0)


if __name__ == '__main__':
    stream = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.sample()

