import tweepy
import datetime
from datetime import timedelta
import webbrowser
import random

consumer_key = '********'
consumer_secret = '********'
access_token = '********'
access_token_secret = '********'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

nowDateObject = datetime.datetime.now()
n = input('When do you wanna unfollow users who tweeted at last?  ')
limitDate = datetime.datetime.today() - timedelta(days=n)

def makeChoice(str, screen_name):
    if str == 'y':
        api.destroy_friendship(screen_name)
    elif str == 'n':
        pass
    elif str == 'o':
        webbrowser.open('https://twitter.com/{user}'.format(user = screen_name))

followList = api.friends_ids('hideo54')
random.shuffle(followList)
for i in followList:
    try:
        newest = api.user_timeline(id=i, count=1)[0]
        if newest.created_at < limitDate:
            lastChoice = raw_input('Do you really wanna unfollow this user, @{user}? (y/n)\nIf you wanna open in your browser, type "o".  '.format(user = newest.user.screen_name))
            makeChoice(lastChoice, newest.user.screen_name)
    except IndexError:
        choice = raw_input('This user, @{user} hasn\'t tweeted yet. Do you wanna unfollow it? (y/n)\nIf you wanna open in your browser, type "o".  '.format(user = newest.user.screen_name))
        makeChoice(choice, newest.user.screen_name)
    except tweepy.error.TweepError:
        print 'An error occurred. It may be caused by API limit. Wait for a while.'
        break
