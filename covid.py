from stream import TwitterStreamListener

# file used to collect tweets about covid for two hours
if __name__ == '__main__':
    KEYWORDS = ['covid', 'covid-19', 'corona', 'coronavirus', 'lockdown']
    # duration 120 times 60 seconds = 2 hours
    duration = 120 * 60

    stream = TwitterStreamListener(duration, 'covid.json')
    stream.filter(track=KEYWORDS)
