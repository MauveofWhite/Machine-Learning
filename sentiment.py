import tweepy
from textblob import TextBlob

consumer_key = "FaYFO6Q0V4vlQCHAyCBxc29HW"
consumer_secret = 'mM0ltGeN7U65wq7aX1G9KRmd0GwdZyrvlpVRJmHjN9LZSbw4yN'

access_token = '1268307797449379840-1ntuNFILaG52PjLn34TdJ79gdisvLz'
access_token_secret = 'CQ71A7glUY3jniQLrxLfKXlAQ4pnQBJ1teRVMlCnxFXSu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
