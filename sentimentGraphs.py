import matplotlib.pyplot as plt
from matplotlib import pyplot
import matplotlib.dates as dates
from dateutil import parser
import datetime
import datetime as dt
import os
import json


datelist =  ['2018-03-28', '2018-03-29', '2018-03-30', '2018-03-31', '2018-04-01',
              '2018-04-02','2018-04-03','2018-04-04', '2018-04-05', '2018-04-07']

polarityData ={}
subjectData={}
extList =[]
path = "./avgsentiments/"

twitterHandles = ['IngrahamAngle', 'davidhogg111', 'FoxNews', 'boycottLauraIngraham','Allstate', 'Arbys']
for handle in twitterHandles:
    for file in os.listdir(path):
        extension = file.split("a")[0]
        print (extension)

        name, ext = file.split(".")
                # open file
        f = open(path + file, 'r')
        data = json.load(f)

        print ("File " + file + " being read.")

        if handle+extension+"sentiments" in data:
            polarity = data.get(handle+extension+"sentiments")[0]
            subject = data.get(handle+extension+"sentiments")[1]

        ext = extension.split("_")[0]
        if ext in extList:
            num = polarityData[ext]
            num2 = subjectData[ext]
            polarityData[ext] = (num+ polarity) / 2
            subjectData[ext] = (num2 + subject) / 2
        else:

            polarityData[extension] = polarity
            subjectData[extension] = subject
            extList.append(extension)
            print(extList)


        print ("file: " + file + " ext: " + extension)


        f.close()

    sortedPolarity={}
    sortedSubject={}
    i=0
    for key in sorted(polarityData):
        sortedPolarity[datelist[i]] = polarityData[key]
        i+=1
    i=0
    for key in sorted(subjectData):
        sortedSubject[datelist[i]] = subjectData[key]
        i+=1

    print(sortedSubject)

    polarDate = list(sortedPolarity.keys())
    polarName = list(sortedPolarity.values())

    subjectDate = list(sortedSubject.keys())
    subjectName = list(sortedSubject.values())



    plt.subplot(2, 1, 1)
    plt.plot(polarDate, polarName, '.-')
    plt.title("@"+ handle +' Average Polarity over Time')
    plt.xlabel('Dates')
    plt.xticks(rotation=45)
    plt.ylabel('Average Polarity')

    plt.subplot(2, 1, 2)
    plt.plot(subjectDate, subjectName, '.-')
    plt.title("@" + handle +' Average Subjectivity over Time')
    plt.xlabel('Dates')
    plt.ylabel('Average Subjectivity')
    plt.xticks(rotation=45)
    plt.tight_layout(h_pad=2.0)
    plt.savefig(handle + '_rtfavs.pdf',bbox_inches='tight')
    plt.show()
