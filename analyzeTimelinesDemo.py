from TwitterModule import *
from dateutil import parser
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import datetime as dt
#from tweetSentimentsDemo import all

twitter_api = oauth_login()#twitter api for grabbing data



class AnalyzeTimeline:

    def __init__(self,n):
        names = []
        names.append(n)
        self.run(names)
    def run(self,names):
        for name in names:
            print("\n" + name)
            nameFile = name + '_timeline' + '.json'
            file = open(nameFile,'w')
            fileCSV = open(name + 'TimelineData.csv','w')

            writer = csv.writer(fileCSV, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            '''
            their codes
            '''
            kw = {  # Keyword args for the Twitter API call
                'count': 200,
                'trim_user': 'true',
                'include_rts' : 'false',
                'since_id' : 1,
                'exclude_replies': 'false',
                'screen_name': name
                }

            results = []
            listDateTimes = []
            listRT = []
            listFav = []
            tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)

            if tweets is None: # 401 (Not Authorized) - Need to bail out on loop entry
                tweets = []
            for tweet in tweets:
                if (tweetInRange(tweet)):
                    datetime = parser.parse(tweet['created_at'])
                    writer.writerow([datetime.strftime("%Y-%m-%d %H:%M:%S"),tweet['retweet_count'],tweet['favorite_count']])
                    listDateTimes.append(datetime.strftime("%Y-%m-%d %H:%M:%S"))
                    listRT.append(tweet['retweet_count'])
                    listFav.append(tweet['favorite_count'])
                    #results[tweet['id']] = [tweet['id'],tweet['created_at'],tweet['retweet_count'],tweet['favorite_count']]
                    results += [datetime.strftime("%Y-%m-%d %H:%M:%S"),tweet['retweet_count'],tweet['favorite_count']]
            running = True

            while(running):

                kw['max_id'] = min([ tweet['id'] for tweet in tweets]) - 1

                tweets = make_twitter_request(twitter_api.statuses.user_timeline, **kw)
                if tweets is None: # 401 (Not Authorized) - Need to bail out on loop entry
                    tweets = []
                for tweet in tweets:
                    if (tweetInRange(tweet)):
                        datetime = parser.parse(tweet['created_at'])
                        writer.writerow([datetime.strftime("%Y-%m-%d %H:%M:%S"),tweet['retweet_count'],tweet['favorite_count']])
                        listDateTimes.append(datetime.strftime("%Y-%m-%d %H:%M:%S"))
                        listRT.append(tweet['retweet_count'])
                        listFav.append(tweet['favorite_count'])
                        #results[tweet['id']] = [tweet['id'],tweet['created_at'],tweet['retweet_count'],tweet['favorite_count']]
                        results += [datetime.strftime("%Y-%m-%d %H:%M:%S"),tweet['retweet_count'],tweet['favorite_count']]

                if (len(tweets) == 0):
                    print("\n\nbroke the loop\n")
                    break

                #completely unecessary
                month = monthNum(tweets[len(tweets)-1]['created_at'][4:7])
                day = int(tweets[len(tweets)-1]['created_at'][8:10])
                year = int(tweets[len(tweets)-1]['created_at'][-4:])
                if (year < 2018):
                    running = False
                else:
                    if (month < 3):
                        running = False
                    elif (month == 3 and day < 25):
                        running = False
                    else:
                        True

            print("ran files")
            json.dump(results,file)
            file.close()
            self.plot(listDateTimes,listRT, listFav, name)
    def plot(self,listDateTimes,listRT, listFav, name):
        #plotting the graphs
        date = dates.datestr2num(listDateTimes)

        plt.subplot(2,1,1)
        plt.plot_date(date, listRT, linestyle = 'solid', aa = 'true', marker = '.', lw = 1)
        plt.ylabel('retweets')
        plt.xticks(rotation=45)
        plt.axvline(dt.datetime(2018,3,29,1,30),c='orange',ls='dashed',lw = 1.0)
        plt.axvline(dt.datetime(2018,3,29,17,6),c='orange',ls='dashed',lw = 1.0)
        plt.title(name + ": retweets per tweet as a functon of time")

        plt.subplot(2,1,2)
        plt.plot_date(date, listFav, linestyle = 'solid', aa = 'true', marker = '.', lw = 1)
        plt.ylabel('favorites')
        plt.xticks(rotation=45)
        plt.axvline(dt.datetime(2018,3,29,1,30),c='orange',ls='dashed', lw=1.0)
        plt.axvline(dt.datetime(2018,3,29,17,6),c='orange',ls='dashed',lw = 1.0)
        plt.title(name + ": favorites per tweet as a functon of time")

        plt.tight_layout(h_pad=2.0)
        plt.show()
        #plt.savefig(name + '_rtfavs.pdf',bbox_inches='tight')
        plt.clf()
if __name__ == "__main__":
  a = sys.argv

  AnalyzeTimeline(a[1])
