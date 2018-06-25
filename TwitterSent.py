import tweepy
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer



consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

arr2 = ""



for status in tweepy.Cursor(api.home_timeline).items(1):
    encoded = status.text.encode("utf-8", errors='ignore')
    for word in status.text:
        if word.isalpha() or word == " " or word == "." or word == "?" or word == "!":
            arr2 += word
        else:
            arr2 += " "


sd = SentimentIntensityAnalyzer()
print(arr2)
print(sd.polarity_scores(arr2))





