import tweepy
from time import sleep
from credentials import *     #import our twitter credentials from credentials.py

auth = tweepy.OAuthHandler( consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


file = open ('verne.txt', 'r')
file_lines = file.readlines()
file.close()








def tweet():
    for line in file_lines:
        try:
            print (line)
            if line != '\n' :
                api.update_status(line)
                sleep(3600)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

tweet()
