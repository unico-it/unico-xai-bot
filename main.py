import os

import tweepy
from unico.client import UnicoApiClient


def generate_tweet():
    unico_client = UnicoApiClient(api_key=os.environ['UNICO_API_KEY'], base_url="https://staging.theunico.it/api")

    result = unico_client.completions.create(agent=os.environ['UNICO_AGENT_NAME'], query="Generate a post about UNICO.")

    x_client = tweepy.Client(
        consumer_key=os.environ['X_API_KEY'],
        consumer_secret=os.environ['X_API_KEY_SECRET'],
        access_token=os.environ['X_ACCESS_TOKEN'],
        access_token_secret=os.environ['X_ACCESS_TOKEN_SECRET'],
    )

    x_client.create_tweet(text=result['text'])


if __name__ == "__main__":
    generate_tweet()
