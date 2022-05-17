import tweepy
import time
from sqlite_connection import insert_data
from textblob import TextBlob
import re


api_key = "" # TWITTER_API_KEY
api_secret_key = "" # TWITTER_API_SECRET
access_token = "" # ACCESS_TOKEN
access_token_secret = "" # ACCESS_SECRET_TOKEN


def autheticate_api_keys():
    # authorize the API Key
    authentication = tweepy.OAuthHandler(api_key, api_secret_key)

    # authorization to user's access token and access token secret
    authentication.set_access_token(access_token, access_token_secret)

    # call the api
    api = tweepy.API(authentication)

    return api


class MyStreamListener(tweepy.StreamListener):
    
    def __init__(self, time_limit=600):
        self.start_time = time.time()
        self.limit = time_limit
        super(MyStreamListener, self).__init__()
    
    def on_connect(self):
        print("Connected to Twitter API.")
        
    def on_status(self, status):
        tweet_date = status.created_at
        tweet_id = status.id # Tweet ID
        print(tweet_id)
        user_id = status.user.id # User ID
        username = status.user.name # Username
        handle = status.user.screen_name
        user_location = status.user.location
        followers_count = status.user.followers_count
        friends_count = status.user.friends_count
        favourites_count = status.user.favourites_count
        status_count = status.user.statuses_count
        verified_status = status.user.verified # boolean value
        acc_creation = status.user.created_at #datetime
        
        # Tweet
        if status.truncated == True:
            tweet = status.extended_tweet['full_text']
            hashtags = status.extended_tweet['entities']['hashtags']
        else:
            tweet = status.text
            hashtags = status.entities['hashtags']

        sentiment = get_tweet_sentiment(tweet=tweet)
        # Read hastags
        hashtags = read_hashtags(hashtags)            
        
        # Retweet count
        retweet_count = status.retweet_count
        # Language
        lang = status.lang
        
        
        # If tweet is not a retweet and tweet is in English
        if not hasattr(status, "retweeted_status") and lang=="en":
            # Connect to database
            insert_data(user_id=user_id, user_name=username, tweet_id=tweet_id, tweet=tweet, retweet_count=retweet_count, hashtags=hashtags,
            handle=handle, user_location=user_location, followers_count=followers_count, favourites_count=favourites_count,
            friends_count=friends_count, status_count=status_count, verified_status=verified_status, acc_creation=acc_creation, 
            tweet_date=tweet_date, sentiment=sentiment)
            
        if (time.time() - self.start_time) > self.limit:
            print(time.time(), self.start_time, self.limit)
            return False
            
    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False

# Extract hashtags
def read_hashtags(tag_list):
    hashtags = []
    for tag in tag_list:
        hashtags.append(tag['text'])
    return hashtags


def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', tweet).split())


def get_tweet_sentiment(tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
