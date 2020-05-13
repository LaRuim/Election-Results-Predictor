import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs

MAXTWEETS = 5000 #Maximum number of tweets after which the code stops, to prevent irrelevant, older data. If we use more hashtags, we will need to increase this number to prevent loss of data

def extract_tweets(page_source): #This function parses the scraped pagesource information
 
    soup = bs(page_source,'lxml')  #lxml is what helps us understand the html data
 
    tweets = []
    for li in soup.find_all("li", class_='js-stream-item'):  #Each tweet is of the same class 'js-stream-item'
        
        flag = 0
        
        if 'data-item-id' not in li.attrs:
            continue
 
        else:
            tweet = {
                'text': None,
                'user_name': None,
                'created_at': None,
                'retweets': 0,
                'likes': 0
            }
 
            # Tweet Text
            text_p = li.find("p", class_="tweet-text")
            if text_p is not None:
                tweet['text'] = text_p.get_text().replace('\n', ' ')

            # Tweet User Name
            user_details_div = li.find("div", class_="tweet")
            if user_details_div is not None:
                tweet['user_name'] = user_details_div['data-name']
 
            # Tweet date
            date_span = li.find("span", class_="_timestamp")
            if date_span is not None:
                a = float(date_span['data-time-ms'])
                tweet['created_at'] = time.ctime(a/1000)
                if a/1000 > 1546300800 and a/1000 < 1558224000:
                    flag = 1
            
            # Tweet Retweets
            retweet_span = li.select("span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount")
            if retweet_span is not None and len(retweet_span) > 0:
                tweet['retweets'] = int(retweet_span[0]['data-tweet-stat-count'])
 
            # Tweet Likes
            like_span = li.select("span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount")
            if like_span is not None and len(like_span) > 0:
                tweet['likes'] = int(like_span[0]['data-tweet-stat-count'])

            if flag == 1:
                tweets.append(tweet)
 
    return tweets


HASHLIST = [] #The list of hashtags whose tweets are scraped

chrome = webdriver.Chrome('/bin/chromedriver') #This is a webdriver, which allows us to manipulate the browser to our convenience

for hashtag in HASHLIST:
   
    # Open the website
    chrome.get('https://twitter.com/Twitter?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor')
   
    # Find the search
    search = chrome.find_element_by_xpath(r'//*[@id="search-query"]')
    time.sleep(0.4)
   
    # Enter the current hashtag
    search.send_keys(hashtag)
   
    # Find the Search button and click it
    search_button = chrome.find_element_by_xpath(r'//*[@id="global-nav-search"]/span/button')
    search_button.click()
    time.sleep(3)
    
    last_height = chrome.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        tweets = chrome.find_elements_by_css_selector("li[data-item-id]")
        time.sleep(3)
        chrome.execute_script("arguments[0].scrollIntoView();", tweets[-1])
        time.sleep(3)
        new_height = chrome.execute_script("return document.body.scrollHeight")
        if new_height == last_height or len(tweets) > MAXTWEETS:
            break
        last_height = new_height

    page_source = chrome.page_source  #Returns the page source
    tweets = extract_tweets(page_source)  #Extracts the html data from the page source and parses it, as described above

    with open('tweets.csv', 'a+') as f:
        for i in tweets:
            count = 0
            for value in i.items():
                f.write('"%s,"' % (value))
                count += 1
                if count > 4:
                    input('This tweet has errors.\n')
            print ('\n', file=f)
   


print('OK')


