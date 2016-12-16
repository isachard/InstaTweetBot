import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler( consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,q='#ocean').items():
    try:
        print ('Tweet by: @' + tweet.user.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
