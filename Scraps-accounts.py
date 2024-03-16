import requests
from bs4 import BeautifulSoup
import re
import time

def scrape_twitter_accounts(twitter_accounts, ticker, interval_minutes):
    while True:
        total_mentions = 0
        for account in twitter_accounts:
            try:

                response = requests.get(f"https://twitter.com/{account}")
                soup = BeautifulSoup(response.text, 'html.parser')
                tweets = soup.find_all('div', class_='tweet')

                for tweet in tweets:
                    tweet_text = tweet.find('div', class_='js-tweet-text-container').text
                    if re.search(r'\b{}\b'.format(re.escape(ticker)), tweet_text, re.IGNORECASE):
                        total_mentions += 1
            except requests.RequestException as e:
                print(f"Error accessing tweets for {account}: {e}")

            time.sleep(5)  


        print(f"{ticker.upper()} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":

    twitter_accounts = [
        "Mr_Derivatives",
        "warrior_0719",
        "ChartingProdigy",
        "allstarcharts",
        "yuriymatso",
        "TriggerTrades",
        "AdamMancini4",
        "CordovaTrades",
        "Barchart",
        "RoyLMattox"
    ]  
    
    ticker = "$TSLA"  
    interval_minutes = 15  

    scrape_twitter_accounts(twitter_accounts, ticker, interval_minutes)
