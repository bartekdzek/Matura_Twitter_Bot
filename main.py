import tweepy
from datetime import date


api_key = ""
api_secret = ""
bearer_token = ""
access_token = ""
access_token_secret =""

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

matura_date = date(2025, 5, 5)
today_date = date.today()
daysleft = matura_date - today_date
daysleft = daysleft.days

new_tweet = f'Do matury 2025 zostało: {daysleft} dni!  #matura2025 #matura2024 #matura'

response = client.create_tweet(text = new_tweet)
print(response)
print('Twitted successfully')
