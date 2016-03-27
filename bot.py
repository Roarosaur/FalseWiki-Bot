import wikipedia
import os
import tweepy
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from secrets import *
from datetime import datetime, timedelta
from time import gmtime, strftime

# individual bot config
bot_username = 'FalseWiki'
logfile_name = bot_username + ".log"
def tweet_bot():
    
    def create_tweet():
        # code for text of tweet here
        
        def random_title():
            title = wikipedia.random(pages=0).encode('utf-8')
            return title
        def random_summary():
            title2 = wikipedia.random(pages=0)
            return wikipedia.summary(str(title2), sentences=1).encode('utf-8')
        
        error = False
        while error == False:
            try:
                uncut_summary = random_summary()
                index_summary = uncut_summary.index(" is ")
            except: 
                error = False
            else:
                error = True

    
        final_title = random_title()
        final_summary = uncut_summary[index_summary:]
        
        text = final_title + final_summary
        return text
    
    def tweet(text):
        # sends text as tweet; twitter auth
        auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
        auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
        api = tweepy.API(auth)
    
        # sends tweet and logs success || failure
        try:
            api.update_status(text)
        except tweepy.error.TweepError as e:
            log(e.message)
        else:
            log ("Tweeted: " + text)
    
    def log(message):
        # logs message to logfile
        path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(path, logfile_name), 'a+') as f:
            t = strftime("%d %b %Y %H:%M:%S", gmtime())
            f.write("\n" + t + " " + (message))
    
    if __name__ == "__main__":
        tweet_text = create_tweet()
        tweet(tweet_text)
        
while 1:
    tweet_bot()

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)
