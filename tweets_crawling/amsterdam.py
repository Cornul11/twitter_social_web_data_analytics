from stream import TwitterStreamListener

# file used to collect tweets in the amsterdam region for two hours
if __name__ == '__main__':
    AMSTERDAM_BOUNDING_BOX = [4.61, 52.27, 5.07, 52.50]
    # duration 120 times 60 seconds = 2 hours
    duration = 120 * 60

    stream = TwitterStreamListener(duration, 'amsterdam.json')
    stream.filter(locations=AMSTERDAM_BOUNDING_BOX)
