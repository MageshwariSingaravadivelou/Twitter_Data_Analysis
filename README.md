## Twitter_Data_Analysis
Various codes to get tweets using Tweepy Package in Python

## File Structure:

```
.
├── README.md                       <-- This is instruction file
├── get_tweets_for_username         <-- Jupyter Notebook to get the latest tweets of the specified user
├── tweet_sentiment_analysis        <-- Sentiment will be identified using TextBlob and piechart will be shown at the end
├── live_twitter_extraction         <-- basic code to get the live twitter data using API (run separately)
│   ├── base.py                     <-- Source functions need to be used in the workflow
│   ├── extract.py                  <-- Functions used for Synthesio extraction
│   └── summary.py                  <-- Summary of extraction based on sources
└── task.py                         <-- Main function used to run the source code parallel
```
## Description
1. Here Tweepy package is used to get the historical tweets and live tweets
2. Tweepy will authenticate the Twitter developer keys and allowed us to extract the data from Twitter
3. Use the modules/packages like OAuthHandler, Stream to authenticate and extract live data respectively

## Requirements:

```
tweepy is a Python library for accessing Twitter API
TextBlob is a Python library for processing textual data (identify the sentiment of data)
RegEx as re, built-in package can be used to work with Regular Expressions
pandas is easy to use open source data analysis and manipulation tool (used to plot pie-graph)
sqlite3 is a server-less database that can be used with python
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install tweepy
pip install TextBlob
pip install re
pip install pandas
pip install sqlite3
```

## Usage

```
main.py contains the main function which is used to go with the flow of process.


To run the code:

python main.py '<keyword>'
The above command will run the code.

```
### Reference
https://developer.twitter.com/en/docs/labs/tweets-and-users/api-reference
https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction
https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction
