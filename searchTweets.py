#import networkx as nx
#import matplotlib.pyplot as plt
import json
import pprint
from TwitterModule import *
import time
from datetime import datetime
#Set up api and global variables
twitter_api = oauth_login()#twitter api for grabbing data

errorLog = open('errorLog.txt','w')
names = ['@IngrahamAngle','@davidhogg111','@sleepnumber','@ATT','@Allstate','@esurance','@Bayer','@RocketMortgage','@LibertyMutual','@Arbys','@TripAdvisor','@Nestle','@hulu','@Wayfair','@FoxNews','#BoycottIngramAdverts','#boycottLauraIngraham','#FireIngraham','#FireLauraIngraham']
for q in names:
    try:
        tweetsDicitonary = {}
        name = q[1:]
        nameFile = name + '328.json'
        file = open(nameFile,'w')

        '''
        First search call to twitter_api
        Parameters:
            q: is the search term
            result_type: is whether we want recent, popular or mixed tweets. Currently set to recent
            max_results: is how many results we wan to take in a single call. Is currently 10 for testing
            until: specifies the date that all tweets returned form this call should come before
                    (so all tweets from this call are from 3/28/2018)

        getMaxID parses the maxID from the appropriate string in the search return metadata
        maxid will then be used to call the next batch of tweets. More info on maxid is Availableon the search api documentation
        '''
        print(q)
        response = make_twitter_request(twitter_api.search.tweets,q=q,result_type='recent',count=5, until = '2018-03-29')
        try:
            next_results = response['search_metadata']['next_results']
            getMaxID = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
            maxid = getMaxID['max_id']
        except:
            next_results = ""
            maxid = 0
            line = "\nretrieval error at " + str(datetime.now()) + " while processing beginning of " + q
            errorLog.write(line)


        '''
        Currently only running 10 times for testing. Figuring out how often to run and how to stop it from running will be a challenge

        Parameters in response:
            most are the same
            -result_type is mixed (testing)
            -max_results is 100 (testing, but really it should be kept like this)
            -max_id field is at the end of the call, allowing each call of the function to retrieve older and older tweets

        time.sleep(5): Can only call the search api 180 times in 15 minutes, so ~5 seconds. Right now set to one because testing, but should probably be set to 10self.
                        Or, we can edit the make-twitter_request function to handle this error for us

        The try:except: is there because this is still unstable. I've encountered errors that I haven't yet figured outself.
            -One big error is when next_results eventually is null, (there are no older tweets to retrieve)
        '''
        for i in range(1,101): #top possible tweets 10,000
            #print(i) #testing code
            try:
                response = make_twitter_request(twitter_api.search.tweets,q=q,result_type='recent',count=100,until = '2018-03-29',max_id=maxid)
                next_results = response['search_metadata']['next_results']
                if (next_results == None):
                    break
                getMaxID  = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
                maxid = getMaxID['max_id']
                print(maxid)
                time.sleep(5)
            except:
                line = "\nretrieval error at " + str(datetime.now()) + " while processing " + q + ' at loop number ' + str(i)
                errorLog.write(line)
                json.dump(tweetsDicitonary,file)
                break
            #print(maxid)
            for tweet in response['statuses']:
                try:
                    tweetsDicitonary[tweet['id']] = tweet
                except:
                    line = "\ndicitonary error at " + str(datetime.now()) + " while processing " + str(tweet['id'])
                    errorLog.write(line)
            #tweetsIngrahamList += str(tweetsIngraham)
            file.seek(0)
            #json.dump(tweetsDicitonary,file) #dumps list/dictionary to file. It can read in as a dictionary that works but I have no idea why. see test.py
        file.seek(0)
        json.dump(tweetsDicitonary,file)
    except:
        line = "\nFatal error at " + str(datetime.now()) + " while processing " + q
        errorLog.write(line)
        json.dump(tweetsDicitonary,file)
