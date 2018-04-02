#import networkx as nx
#import matplotlib.pyplot as plt
import json
from TwitterModule import *

#Set up api and global variables
twitter_api = oauth_login()#twitter api for grabbing data
tweetsIngraham = {}

q = 'IngrahamAngle'
#statuses = twitter_search(twitter_api.search.tweets,q, max_results=10, until=2018-03-27)
#statuses = make_twitter_request(twitter_api.search.tweets,q, max_results=10, until=2018-03-27)
#print statuses

#q = "CrossFit"
for
results = twitter_search(twitter_api, q, result_type='recent',max_results=10)
resultsJSON = json.loads(results)
tweetsIngraham.append(resultsJSON['statuses'])
#print json.dumps(results['statuses'],indent-1)
#print json.dumps(results[0], indent=1)
