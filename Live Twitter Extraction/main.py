import tweepy
import sys
from live_twitter_extraction import MyStreamListener, autheticate_api_keys
from sqlite_connection import create_database

        
if __name__=="__main__":
    # topic = sys.argv[1]
    topic = ['Xbox Series X']
    
    create_database()
    # Streaming tweets
    myStreamListener = MyStreamListener()
    api = autheticate_api_keys()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, tweet_mode="extended")
    myStream.filter(track=topic)
