from stream import TwitterStreamListener

# file used to sample 10 minutes of the public twitter stream
if __name__ == '__main__':
    # duration 10 times 60 seconds = 10 minutes
    duration = 60 * 10

    stream = TwitterStreamListener(duration, 'public.json')
    stream.sample()
