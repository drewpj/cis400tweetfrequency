#import networkx as nx
#import matplotlib.pyplot as plt
import json
import pprint
from TwitterModule import *
import time
from datetime import datetime
#Set up api and global variables
twitter_api = oauth_login()#twitter api for grabbing data
#dates = [330,331,401,402,403]
dates = [401,402,403,404,405,406,407]

for day in dates:
    print(day)
    names = ['@itsnotdrew','@davidhogg111','@IngrahamAngle','@sleepnumber','@ATT','@Allstate','@esurance','@Bayer','@RocketMortgage','@LibertyMutual','@Arbys','@TripAdvisor','@Nestle','@hulu','@Wayfair','@FoxNews','#BoycottIngramAdverts','#boycottLauraIngraham','#FireIngraham','#FireLauraIngraham']
    errorLogName = 'errorLog' + str(day) + '_4' +  '.txt'
    errorLog = open(errorLogName,'w')
    for q in names:
        try:
            dateStr = str(day)
            dateDay = dateStr[1:]
            dateDayPlusOne = str(int(dateDay)+1)
            dateMonth = dateStr[0]

            if (dateStr == '331'): #dirty code to fix a logic bug when switching months
                dateDayPlusOne = '01'
                dateMonth = '4'

            until = '2018-0' + dateMonth + '-' + dateDayPlusOne
            tweetsDicitonary = {}
            name = q[1:]
            nameFile = name + dateStr +'_4'+  '.json'
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
            maxid will then be used to call the next batch of tweets. More info on maxid is Available on the search api documentation
            '''
            print(q + 'at ' + str(datetime.now())) #prints twitter user being processed

            response = make_twitter_request(twitter_api.search.tweets,q=q,result_type='recent',count=5, until=until)
            try:
                next_results = response['search_metadata']['next_results']
                getMaxID = dict([ kv.split('=') for kv in next_results[1:].split("&") ])
                maxid = getMaxID['max_id']
            except:
                next_results = ""
                maxid = 0
                line = "\nretrieval error at " + str(datetime.now()) + " while processing beginning call of " + q
                errorLog.write(line)

            '''
            Parameters in response:
                most are the same
                -result_type is mixed (testing)
                -max_results is 100 (testing, but really it should be kept like this)
                -max_id field is at the end of the call, allowing each call of the function to retrieve older and older tweets

            time.sleep(5): Can only call the search api 180 times in 15 minutes, so ~5 seconds. Right now set to one because testing, but should probably be set to 10self.
                            Or, we can edit the make-twitter_request function to handle this error for us

            '''
            for i in range(1,101): #top possible tweets 10,000
                #print(i) #testing code
                try:
                    response = make_twitter_request(twitter_api.search.tweets,q=q,result_type='recent',count=100,until=until,max_id=maxid)
                    next_results = response['search_metadata']['next_results']
                    if (next_results == None):
                        break
                    getMaxID  = dict([ kv.split('=') for kv in next_results[1:].split("&") ])#to get the nextID
                    maxid = getMaxID['max_id']
                   # print(maxid)
                    time.sleep(5)
                except:
                    line = "\nretrieval error at " + str(datetime.now()) + " while processing " + q + ' at loop number ' + str(i)
                    errorLog.write(line)
                    break
                for tweet in response['statuses']:#add each tweet to a dictionary
                    try:
                        tweetsDicitonary[tweet['id']] = tweet
                    except:
                        line = "\ndicitonary error at " + str(datetime.now()) + " while processing " + str(tweet['id'])
                        errorLog.write(line)
                file.seek(0)
            file.seek(0)
            json.dump(tweetsDicitonary,file)
            file.close()
        except:
            line = "\nFatal error at " + str(datetime.now()) + " while processing " + q
            errorLog.write(line)
            json.dump(tweetsDicitonary,file)
            file.close()
