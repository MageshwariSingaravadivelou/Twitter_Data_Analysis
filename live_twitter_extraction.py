#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API 
consumer_key = "oqWfLQA5EH4YMIrBYa1HxfriT" # TWITTER_API_KEY
consumer_secret = "HD0voPZPl6YNYsTMh7pKMvzsUItlqtaHuJYNkzLIYZbk39DuCB" # TWITTER_API_SECRET
access_token = "1157237591906766848-D2157SfTIIy2J0gaN27Wa98WWpsZBz" # ACCESS_TOKEN
access_token_secret = "5I4FwGwI72iZWTI9HHTChied5yzlebDptwbrCDQ7zbyM3" # ACCESS_SECRET_TOKEN


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['xbox'])