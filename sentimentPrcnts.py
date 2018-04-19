import os
import json

#go through sentiments_by_company directory
for folder in os.listdir("./sentiments_by_company"):
    path = "./sentiments_by_company/" + folder + "/"
    print path
    percent = {}

    #go through each file within company folder
    for file in os.listdir(path):
        #ignore hidden files and newly created file
        if not file.startswith('.') and not file.startswith("percent"):
            #split file name to get company and date for new dictionary key
            name,ext = file.split("sentiments",)
            #reset values to 0
            possent = 0
            negsent = 0
            nosent = 0
            try:
                print file
                f = open(path + file, 'r')
                sentiments = json.load(f)
                #make sure dictionary exists
                if sentiments:
                    for (k, v) in sentiments.values():
                        if (k > 0):
                            possent += 1
                        elif (k < 0):
                            negsent += 1
                        else:
                            nosent += 1
                    print len(sentiments)
                    #get percentages
                    posprct = (float(possent) / len(sentiments)) * 100
                    print posprct
                    negprct = (float(negsent) / len(sentiments)) * 100
                    print negprct
                    noprct = (float(nosent) / len(sentiments)) * 100
                    print noprct
                    percent[name] = (posprct, negprct, noprct)
                f.seek(0)
                f.close()
            #general except if it breaks
            except:
                print "Error for " + file + " in " + path
                break
    #put stuff in new file after all the files in each folder are read
    newfile = open(path + "/percentages.json", 'w')
    json.dump(percent, newfile)
    newfile.seek(0)
    newfile.close()