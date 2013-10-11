import sys
import tweepy

CONSUMER_KEY = 'xxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxx'

if (len(sys.argv) > 1):
    tweetFile = sys.argv[1]
else:
    tweetFile = "/tmp/tweets.txt"

f = open(tweetFile, "r")
tweetList = f.readlines()
f.close()
try:
    firstTweet = tweetList.pop(0)
except Exception as e:
    sys.exit(0)

# If we made it this far, the tweet file must have tweets.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
try:
    api.update_status(firstTweet)
    print "Tweet sent: " + firstTweet
except Exception as e:
    print "Error sending tweet [" + str(len(firstTweet)) + " length]: " + firstTweet

f = open(tweetFile, "w")
for i in tweetList:
    f.write(i)
f.close()
