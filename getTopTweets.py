'''
getTopTweets.py
Get the top 20 possitive, negative, and neutral tweets for a specific day for a specific user
Run by typing the username+day
ex: for Nestle on March 23rd, type Nestle328
'''
import cPickle
import sys

class getTopTweets:
    def __init__(self,n):
        self.run(n)

    def run(self,name):
            '''
            Initialize variables and open file
            '''
            path = "./sentiments/"
            print path
            files = []
            fileTypeStr = ["Neu","Neg","Pos"]
            fileStr = ["Neutral:","Negative:","Positive:"]
            i = 0

            #For each pos, neg, neu files
            for type in fileTypeStr:
                try:
                    files.append(open(path + name + type + ".txt", 'r'))
                    i = i + 1
                except Exception,e:
                    print(str(e))
                    print("file " + path + name + type + ".txt failed to open")
            i = 0
            for f in files:#for each file we found
                print("\n\n\n" + fileStr[i] + "--------------------------------------------------------------------------------------------------------------------------------")
                self.printTopTen(f)
                i = i + 1

    def printTopTen(self,file):
         list = cPickle.load(file)

         for i in range(0,20):#load top 20
             try:
                 print("** "+list[i])
             except Exception,e:
                 print(str(e))
         file.close()

if __name__ == "__main__":
  a = sys.argv
  getTopTweets(a[1])
