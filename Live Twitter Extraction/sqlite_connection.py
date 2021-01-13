import sqlite3
import time
from sqlite3 import Error


db_name = 'live_twitter_test1.db'
topic = 'Xbox'

def create_database():

    conn = sqlite3.connect(db_name)

    # Table creation
    commands = (# Table 1
                '''Create Table TwitterUser(User_Id BIGINT PRIMARY KEY, User_Name TEXT,
                User_Handle TEXT, User_Location TEXT, Followers_Count INT,
                Friends_Count INT, Favourites_Count INT, Statuses_Count INT,
                Created_At DATETIME, Verified_Status BOOLEAN);''',
                # Table 2
                '''Create Table TwitterTweet(Created_At DATETIME, Topic TEXT,
                                            Tweet_Id BIGINT PRIMARY KEY,
                                            User_Id BIGINT,
                                            Tweet TEXT,
                                            Sentiment TEXT,
                                            Retweet_Count INT,
                                            CONSTRAINT fk_user
                                                FOREIGN KEY(User_Id)
                                                    REFERENCES TwitterUser(User_Id));''',
                # Table 3
                '''Create Table TwitterEntity(Id PRIMARY KEY, Created_At DATETIME,
                                            Tweet_Id BIGINT,
                                            Hashtag TEXT,
                                            CONSTRAINT fk_user
                                                FOREIGN KEY(Tweet_Id)
                                                    REFERENCES TwitterTweet(Tweet_Id));''')

    # Create cursor to execute SQL commands
    cur = conn.cursor()

    # Execute SQL commands
    for command in commands:
        try:
        # Create tables
            cur.execute(command)
        except sqlite3.OperationalError:
            pass

    # Close communication with server
    conn.commit()
    cur.close()
    conn.close()


# Insert Tweet data into database
def insert_data(user_id, user_name, tweet_id, tweet, retweet_count, hashtags, handle, user_location,
                followers_count, favourites_count, friends_count, status_count, 
                verified_status, acc_creation, tweet_date, sentiment):
        # conn = psycopg2.connect(host="localhost",database="TwitterDB",port=5432,user=<user>,password=<password>)
    conn = sqlite3.connect(db_name)
    
    cur = conn.cursor()
    try:
        # insert user information
        command = "INSERT INTO TwitterUser (User_Id, User_Name, User_Handle, User_Location, Followers_Count, Friends_Count, Favourites_Count, Statuses_Count, Created_At, Verified_Status) VALUES (?,?,?,?,?,?,?,?,?,?)"
        params = (user_id, user_name, handle, user_location, followers_count, favourites_count, friends_count, status_count, acc_creation, verified_status)
        cur.execute(command, params)

        # insert tweet information
        command = "INSERT INTO TwitterTweet (Created_At, Topic, Tweet_Id, User_Id, Tweet, Sentiment, Retweet_Count) VALUES (?,?,?,?,?,?,?);"
        params = (tweet_date, topic, tweet_id, user_id, tweet, sentiment, retweet_count)
        cur.execute(command, params)
    
        # insert entity information
        for i in range(len(hashtags)):
            hashtag = hashtags[i]
            command = "INSERT INTO TwitterEntity (Created_At, Tweet_Id, Hashtag) VALUES (?,?,?);"
            params = (tweet_date, tweet_id, hashtag)
            cur.execute(command, params)

    except sqlite3.IntegrityError:
        time.sleep(10)
        pass
    # Commit changes
    conn.commit()
    
    # Disconnect
    cur.close()
    conn.close()
