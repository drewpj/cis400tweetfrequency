import os
import json

for folder in os.listdir("./sentiments"):
    path = "./sentiments/" + folder + "/"
    newfile = open(folder + "avgsentiments.json", 'w')
    print path
    avgsentiments = {}

    # ignore hidden files/folders
    if not folder.startswith('.'):
        try:
            # go through each file in folder
            for file in os.listdir(path):
                name, ext = file.split(".")
                f = open(path + file, 'r')
                sentiments = json.load(f)
                print "File " + file + " being read."
                psum = 0
                ssum = 0
                if sentiments:
                    for polarity, subjectivity in sentiments.values():
                        psum+=polarity
                        ssum+=subjectivity
                    avgpolarity = psum/len(sentiments)
                    avgsubjectivity = ssum/len(sentiments)
                    avgsentiments[name] = (avgpolarity,avgsubjectivity)
                f.seek(0)
                f.close()
            json.dump(avgsentiments, newfile)
            newfile.seek(0)
            newfile.close()
        except:
            print "Error for " + file + " in " + path
            break
