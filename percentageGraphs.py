import matplotlib.pyplot as plt
from datetime import date
import collections
import os
import json


#go through each folder in directory
for folder in os.listdir("./sentiments_by_company"):
    path = "./sentiments_by_company/" + folder + "/"

    avgsentiments = {}

    #open file percentages.json from the folder
    f = open(path+"percentages.json", 'r')
    #load contents from the file
    sentiments = json.load(f)

    keys= sentiments.keys()
    values= sentiments.values()

    newKeys=[]

    n= len(folder)
    #this dictionary will be used in graphing the data
    #OrderedDict() keeps the keys and values in approporiate sorted order
    avgSents=collections.OrderedDict()

    print keys
    for key in keys:
        str = key
        splitat = n

        #the key is the name of a twitter handle and a date
        #split the key to separate the twitter handle and the date
        k, v = str[:splitat], str[splitat:]

        #create a list of new keys, each key is now the date
        newKeys.append(v)



    i=0
    for x in sorted(newKeys):
        #split the string to get the month and day separately
        mon,day = x[:1], x[1:]

        try:
            #use the datetime module, to put the date in YYYY- MM - DD format
            newDate = date(2018, int(mon), int(day))
        except ValueError:
            pass
        #change the keys to the new date format
        avgSents[newDate] = sentiments[keys[i]]
        i+=1


    #3 dictionaries, used for graphing three separate lines
    pos = collections.OrderedDict() #contains percentage of positive sentiment tweets
    neg = collections.OrderedDict() # contains percentage of negative sentiment tweets
    neutral = collections.OrderedDict()  # contains percentage of neutral sentiment tweets

    #fill in the dictionaries with data from the the avgSents diciontary
    for k,v in avgSents.items():
        pos[k]=v[0]
        neg[k]=v[1]
        neutral[k]=v[2]

    #plot 3 separate lines
    plt.plot(pos.keys(), pos.values(), 'o-', label='positive', color='blue')
    plt.plot(neg.keys(), neg.values(), 'o-', label='negative', color ='red')
    plt.plot(neutral.keys(), neutral.values(), 'o-', label='neutral', color='gold')


    #label the axis, title, create a legend
    plt.title(folder+" Tweet Classification")
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.ylabel('Polarity Percentage Distribution')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    #save graph the the computer
    plt.tight_layout(h_pad=2.0)
    plt.savefig(folder + '.pdf',bbox_inches='tight')
    plt.show()
