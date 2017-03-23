import tweepy
from tweepy import OAuthHandler
import json
from datetime import datetime
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
results=[]
with open('tweets.json', 'a') as json_file:
	while True:
		tweets =api.search(q='#DonaldTrump',rpp=100)
		# insert code here to fetch tweets
		if tweets:
			for tweet in tweets:
				json_tweet = tweet._json # convert to JSON format
				# Write the tweet to tweets.json
				json.dump(json_tweet,json_file)
				json_file.write('\n')
		else:
			break