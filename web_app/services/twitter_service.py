import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.environ.get("TWITTER_API_KEY")
consumer_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
print ("Auth", type(auth))

api = tweepy.API(auth)

if __name__ == "__main__":
    user = api.get_user("s2t2")

    tweets = api.user_timeline("s2t2", tweet_mode="extended", count=150)

    for tweet in tweets:
       print("----")
       print(tweet.id, tweet.full_text)

