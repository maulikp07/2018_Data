import tweepy
from textblob import TextBlob

consumer_key = 'Hry8rNVGfw5PwuECEokWZayzw'
consumer_secret = 'CmmEXWQ2V9iaWV56pDaXjZtXFCXmkf1bPugywvRnuZyJdGaV03'


access_token = '4563767532-fLjOinXJklPzYaY439yjhMUTwwA8sdVWfdkt4QM'
access_token_secret = '9VHlnY9JImNqSuxqtPuQoJSYjOqZDFVC4F94JINljs5eB'

auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets :
    print(tweet.text)

