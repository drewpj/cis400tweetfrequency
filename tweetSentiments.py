from textblob import TextBlob
import json
import os

#can clean up so we don't need to list out the names of folders, but works for now
folders = ["328", "330_3", "331", "331_2", "401_3", "401_4", "402", "402_2", "402_3", "404_4", "405_4"]

#go through each folder in data
for folder in folders:
    #manuallly make path
    path = "./data/" + folder +"/"
    print path

#go through each file in each folder
    for file in os.listdir(path):
        name, ext = file.split(".")
        #open file
        f = open(path+file, 'r')
        tweets = json.load(f)
        print "File " + file + " being read."
        #initialize dictionary for sentiments
        sentiments = {}
        #used to get the keys, probably better way to do it
        i = 0

        #go through each tweet
        for tweet in tweets.values():
            k = tweets.keys()[i]
            #tweetblob just the actual tweet and get the sentiment
            tweetblob = TextBlob(tweet["text"])
            sentiment = tweetblob.sentiment
            #add to dictionary with user id as the key
            sentiments[k] = sentiment
            i += 1
        f.seek(0)
        f.close()
        #create new file to dump the data to
        newfile = open(path+name+"sentiments", 'w')
        json.dump(sentiments, newfile)
        newfile.seek(0)
        newfile.close()