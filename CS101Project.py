import sys
sys.path.insert(0, './modules')

from trainClassifiers import Train
from tweetScraper import Scrape
from sentimentCalculator import calculateSentiments
from CSVtoPickle import pickleTweets

#Train()
#Scrape()
calculateSentiments()
pickleTweets()
