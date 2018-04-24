from textblob import TextBlob
import json
import os
import pickle

#in order for this to work, all folders must be within a "data" folder

#go through each folder in data
class sentiments:
    for folder in os.listdir("./data"):
        #manuallly make path
        path = "./data/" + folder +"/"
        print path

    #ignore hidden files/folders
        if not folder.startswith('.'):
            #try:
            #go through each file in folder
            for file in os.listdir(path):
                name, ext = file.split(".")
                # open file
                f = open(path + file, 'r')
                tweets = json.load(f)
                print "File " + file + " being read."
                # initialize dictionary for sentiments
                sentiments = {}
                # used to get the keys, probably better way to do it
                i = 0
                pos = []
                neu = []
                neg = []
                # go through each tweet
                # in order for this to work, all files must be tweet dictionaries -
                # no error logs or any other type of file can be in the folders
                for tweet in tweets.values():
                    k = tweets.keys()[i]
                    # tweetblob just the actual tweet and get the sentiment
                    tweetblob = TextBlob(tweet["text"])
                    sentiment = tweetblob.sentiment.polarity
                    if (sentiment == 0):
                        neu.append(tweet["text"])
                    if (sentiment > 0):
                        pos.append(tweet["text"])
                    if (sentiment < 0):
                        neg.append(tweet["text"])


                    # add to dictionary with user id as the key
                    sentiments[k] = sentiment
                    i += 1
                f.seek(0)
                f.close()
                # create new file to dump the data to
                sentimentList = [neg,neu,pos]
                typeSentiment = ['Neg','Neu','Pos']
                i = 0
                for sent in typeSentiment:
                    sentFile = open("./sentiments/" + name + sent + ".txt", 'w')
                    sentFile.seek(0)
                    json.dump(sentimentList[i], sentFile)
                    sentFile.close()
                    i = i + 1
            #general except for when it breaks
            '''
            except:
                print "Error for " + file + " in " + path
                break
            '''
