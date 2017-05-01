import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
# Fill with your API keys
consumer_key= ''
consumer_secret= ''

access_token=''
access_token_secret=''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def sentiment_polarity(tweet):
    if tweet.sentiment.polarity > 0:
        return 'Positive'
    else:
        return 'Negative'

polarities= []

tweets = api.search(q=["north korea", 'trump'], count = 100)
with open('tweets.csv', 'wb') as csvfile:
    csvfile.write('tweet, label\n')
    for tweet in tweets:
        analysis = TextBlob(tweet.text)
        polarities.append(analysis.sentiment.polarity)
        csvfile.write('%s,%s\n' % ((tweet.text.encode('utf8')), sentiment_polarity(analysis)))

'''
for tweet in public_tweets:
    print(tweet.text)

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
'''
