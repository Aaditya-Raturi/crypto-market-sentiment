import tweepy
import requests
import pandas as pd

# Replace with your Twitter API keys
consumer_key = 'Jpez4kpy2dzQv7EF4vjhMkxrb'
consumer_secret = '2qCK25vTgLZLCBlIgU4Zsb27J26b1inCVZ017eLXXmSDLEcPcH'
access_token = '1308778544366006273-NmTK2TrrcoWlorwQaCLVck2h8RZSkI'
access_token_secret = 'PSc1QdpYD0W23mZtJsiANXmQe60gmrxI4JbyDBxEbmr0H'

# Set up the Twitter API client using Tweepy
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Function to fetch tweets about a specific crypto
def fetch_tweets(keyword, count=100):
    tweets = api.search(q=keyword, count=count, lang='en', tweet_mode='extended')
    tweet_data = [{'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
    return pd.DataFrame(tweet_data)

# Function to fetch current price of a cryptocurrency using CoinGecko API
def fetch_crypto_price(crypto_id="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()[crypto_id]["usd"]

# Example usage
if __name__ == "__main__":
    crypto_name = "bitcoin"
    print(f"Fetching tweets for {crypto_name}...")
    tweets_df = fetch_tweets(crypto_name, 50)
    print(f"Fetched {len(tweets_df)} tweets.")
    
    print(f"\nFetching {crypto_name} price...")
    price = fetch_crypto_price(crypto_name)
    print(f"The current price of {crypto_name} is ${price}")
    
    # Save the tweets to a CSV file
    tweets_df.to_csv(f'{crypto_name}_tweets.csv', index=False)
    print(f"Tweets saved to {crypto_name}_tweets.csv")

