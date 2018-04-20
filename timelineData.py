from TwitterModule import *
twitter_api = oauth_login()#twitter api for grabbing data

class AnalyzeTimeline:
    def __init__(self,):
        self.run()
    def run(self):
        #names = ['Nutrish']
        names = ['nutrish','davidhogg111','IngrahamAngle','sleepnumber','ATT','Allstate','esurance','Bayer','RocketMortgage','LibertyMutual','Arbys','TripAdvisor','Nestle','hulu','Wayfair','FoxNews']
        for name in names:
            print("\n" + name)
            tweets = harvest_user_timeline(twitter_api, screen_name=name, max_results=800)

            lauraTweets = {}
            nonLauraTweets = {}

            for tweet in tweets:
                if (self.checkDate(tweet['created_at'])):
                    if (self.ifLaura(tweet['text'])):
                        lauraTweets[tweet['id']] = tweet
                    else:
                        nonLauraTweets[tweet['id']] = tweet
            #self.printAndWrite(lauraTweets,nonLauraTweets)
            lauraFav = self.getAvFavs(lauraTweets)
            nonLauraFav = self.getAvFavs(nonLauraTweets)
            print("Average favorites for tweets mentioning 'Ingraham': " + str(lauraFav))
            print("Average favorites for tweets not mentioning 'Ingraham': " + str(nonLauraFav))


    def checkDate(self,created):
        month = monthNum(created[4:7])
        day = int(created[8:10])
        year = int(created[-4:])
        if (year < 2018):
            return False
        else:
            if (month < 3):
                return False
            elif (month == 3 and day < 25):
                return False
            else:
                return True

    def ifLaura(self,text):
        '''
        if "laura" in tweet['text']:
            return True
        elif "Laura" in tweet['text']:
            return True
        '''
        if "Ingraham" in text:
            return True
        return False
    def printAndWrite(self,lt,nlt):
        print("Printing")
        print len(lt)
        for key in lt.keys():
            print lt[key]['favorite_count']
    def getAvFavs(self,tweets):
        avg = 0.0;
        for key in tweets.keys():
            avg = avg + int(tweets[key]['favorite_count'])
        if (len(tweets) == 0):
            return 0
        else:
            avg = float(avg) / float(len(tweets))
            return avg

if __name__ == "__main__":
  #a = sys.argv
  AnalyzeTimeline()
