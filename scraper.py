#Credit to Marco Bonzanini

import tweepy
import json
from tweepy import OAuthHandler

consumer_key = 'KGrJyI9GdujKcowMfrheB78dR'
consumer_secret = 'TEa81xn0OZOwebVyNccqQFkY2Qe0qPJbHixz1GZQZlJZ55jY2V'
access_token = '3021600922-wF6n5jmtjnd6Ip16L3CguHxK4p19OblPXjvJYvF'
access_secret = 'fVpGcfRkzJB0C0lyRUEMr7lGOhz8j1cBQ8PUyQx4FWzaK'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# the 10 is an arbitrary value
# using too much bandwidth puts the Twitter Police on you
#for status in tweepy.Cursor(api.home_timeline).items(10):
    # process just one status
    # I think a status is like a post?
#    print(status.text)

f = open("scrapings.text", "w+")
timeline = api.user_timeline(screen_name = "56b3197f775b41a", include_rts = True, count=10)
for tweet in timeline:
    print(tweet.text)
    f.write(tweet.text + "\n")

#for tweet in tweepy.Cursor(timeline).items():
 #   print(tweet.text + "\n")
  #  f.write(tweet.text + "\n")