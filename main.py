from textblob import TextBlob
import tweepy
import sys

# Acquire keys and tokens from the Twitter Developer Portal

API_KEY = '!YOUR KEY HERE!'
API_KEY_SECRET = '!YOUR KEY HERE!'

ACCESS_TOKEN = '!YOUR TOKEN HERE!'
ACCESS_TOKEN_SECRET = '!YOUR TOKEN HERE!'

authHandler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET)
authHandler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

API = tweepy.API(authHandler)

searchTerm = '!YOUR TOPIC OF CHOICE!' # Place the topic here.
tweetAmount = 100 # Amount of tweets that will be analyzed

tweets = tweepy.Cursor(API.search_tweets, q=searchTerm, lang='en').items(tweetAmount)

polarity = 0

positive = 0
neutral = 0
negative = 0

# Cleaning up the returned text so that it is easier to read and analyze.

for tweet in tweets:
    final_text = tweet.text.replace('RT', '') 

    # Removes any usernames from the text

    if final_text.startswitch(' @'):
        position = final_text.index(':')            
        final_text = final_text[position+2:]  
        
    if final_text.startswitch('@'):
        position = final_text.index(' ')            
        final_text = final_text[position+2:]    
    
    print(final_text)

    analysis = TextBlob(final_text)
    tweetPolarity = analysis.polarity

    if tweetPolarity > 0.00:
        positive += 1
    elif tweetPolarity < 0.00:
        negative += 1
    elif tweetPolarity == 0.00:
        neutral += 1

    polarity += analysis.polarity





print(f'Overall polarity: {polarity}') # If the number printed is greater than 0, the tweet is overall positive. If the number printed is less than 0, the tweet is overall negative. If the number printed is 0, the tweet is neutral.
print(f'Amount of positive tweets: {positive}')
print(f'Amount of negative tweets: {negative}')
print(f'Amount of neutral tweets: {neutral}')