# Matura_Twitter_Bot
Daily Countdown to Matura 2025 on Twitter(X)

Daily Countdown to Matura 2025 on Twitter
This project is designed to post a daily countdown to the Matura 2025 exam on Twitter, leveraging the Tweepy library to interact with the Twitter API. The countdown tweets provide an update on the number of days left until the exam, helping students stay aware of the time remaining.

Features
Automated Daily Tweets: The script calculates the number of days remaining until the Matura 2025 exam and posts a tweet every day with the countdown.
Scheduled Execution: The script is hosted on PythonAnywhere, which allows it to run daily without the need for manual intervention.
Twitter API Integration: Using the Tweepy library, the script authenticates with the Twitter API and posts updates to the account @Ilednido_matury.
Technical Details
Programming Language: Python
Libraries Used:
tweepy for interacting with the Twitter API.
datetime for calculating the days left until the exam.
Deployment: The script runs on PythonAnywhere, a cloud-based Python development environment, ensuring it executes reliably every day.
Code Overview
python
Skopiuj kod
import tweepy
from datetime import date

# Twitter API credentials
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Initialize Tweepy client
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Calculate days left until Matura 2025
matura_date = date(2025, 5, 5)
today_date = date.today()
daysleft = matura_date - today_date
daysleft = daysleft.days

# Create and post tweet
new_tweet = f'Do matury 2025 zostało: {daysleft} dni!  #matura2025 #matura2024 #matura'
response = client.create_tweet(text=new_tweet)
print(response)
print('Twitted successfully')
How to Use
Clone the Repository: Clone the repository to your local machine.
Set Up Twitter API Credentials: Replace the placeholder values in the script with your actual Twitter API credentials.
Deploy on PythonAnywhere: Upload the script to PythonAnywhere and set up a daily task to run the script.
Future Enhancements
Customization: Add functionality to customize the message format and hashtags.
Error Handling: Implement robust error handling and logging for better monitoring and troubleshooting.
Feel free to check out the Twitter account @Ilednido_matury to see the daily countdown in action!

This description should provide a comprehensive overview of your project, its functionality, and how to use it. It also highlights the use of PythonAnywhere for automation and includes the necessary links to your Twitter profile and PythonAnywhere.








