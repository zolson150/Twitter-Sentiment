import nltk
import random
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import tweepy
from tweepy import OAuthHandler
import string

strings = twitter_samples.strings('negative_tweets.json')
strings2 = twitter_samples.strings('positive_tweets.json')
stop_words = set(stopwords.words("english"))
tknzr = TweetTokenizer()

tweet2 = ""
tweet = ""
positive_tweets = []
all_pos_words = []
negative_tweets = []
all_neg_words = []


consumer_key = 'qvDezLUCBtGKkRICGHit8aX1D'
consumer_secret = 'qj32TdPz8ttq4q2H2avrFHdgXOOKVdF0sIWT06jE2dJeGzZyAJ'
access_token = '1010249200641236998-tAVWj1WT8Jxo2SsUoAdWzM1TpY2VCZ'
access_secret = 'gk0OUE3YiLWxEuTVK370yuSG10jQQuZIyDR4QsgUp2GBt'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


for status in tweepy.Cursor(api.home_timeline).items(1):
    encoded = status.text.encode("utf-8", errors='ignore')
    tweet2 = status.text
    for word in status.text:
        if word.isalpha() or word == " " or word == ".":
            tweet += word
        else:
            tweet += " "

for string in strings[:1000]:
    split_string = string.split()
    for word in split_string:
        if word not in stop_words:
            negative_tweets.append(word)
        

for string in strings2[:1000]:
    split_string = string.split()
    for word in split_string:
        if word not in stop_words:
            positive_tweets.append(word)

all_neg_words = nltk.FreqDist(negative_tweets)
all_pos_words = nltk.FreqDist(positive_tweets)


def sentiment_feature(word):

    positive = negative = 0
    tweet = tknzr.tokenize(word)
    
    for words in tweet:
        
        if all_pos_words[words] > all_neg_words[words]:
            negative += 1
        elif all_pos_words[words] < all_neg_words[words]:
            positive += 1
        
    if positive > negative:
        return {'Positive words ' : positive}
    else:
        return {'Negative words ' : negative}

labeled_tweets = ([(string, 'Negative') for string in strings[1000:]] +
                  [(string, 'Positive') for string in strings2[1000:]])

random.shuffle(labeled_tweets)

feature_sets = [(sentiment_feature(n), sentiment) for (n, sentiment) in labeled_tweets]
train_set = feature_sets[500:]
test_set = feature_sets[:500]

classifier = nltk.NaiveBayesClassifier.train(train_set)
print(tweet2)
print(classifier.classify(sentiment_feature(tweet)))


