# tweets_from_txt.py
tweets_from_txt is a pretty straightforward script. It makes use of the "tweepy" python library to pop a tweet off the end of a text file, and fire it off using whatever credentials were set in lines 4, 5, 6, an 7.

It accepts one argument (the name of the text file containing tweets). The delimiter separating tweets in the text file are linebreaks! Basically, I wanted to be able to setup a cronjob that would fire off manually typed tweets at a specific interval and then removed the tweet off the end after each execution.

There's some pretty nice GUI apps out there (Hootsuite) that already do this, but I liked the appeal of just filling up a text file and letting the cronjob do the rest.

**Example of usage:**

```bash
$ python tweet_from_txt.py /Users/Documents/text_file_containing_tweets.txt
```
