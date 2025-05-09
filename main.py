import os

import tweepy
import unico


def generate_tweet():
    unico_client = unico.Client(api_key=os.environ['UNICO_API_KEY'], base_url="https://staging.theunico.it/api")
    x_client = tweepy.Client(
        consumer_key=os.environ['X_API_KEY'],
        consumer_secret=os.environ['X_API_KEY_SECRET'],
        access_token=os.environ['X_ACCESS_TOKEN'],
        access_token_secret=os.environ['X_ACCESS_TOKEN_SECRET'],
        bearer_token=os.environ['X_BEARER_TOKEN']
    )

    tweets = x_client.search_recent_tweets(query="#Innovation", max_results=10)
    tweet_texts = [tweet.text for tweet in tweets.data]

    prompt = "Based on the following tweets generate a post to promote UNICO: " + " ".join(tweet_texts)
    result = unico_client.agent(os.environ['UNICO_AGENT_ID']).completions.create(prompt)

    x_client.create_tweet(text=result['text'])


if __name__ == "__main__":
    generate_tweet()
