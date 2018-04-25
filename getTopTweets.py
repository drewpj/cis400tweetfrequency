import cPickle
import sys
#from tweetSentimentsDemo import all

class getTopTweets:
    def __init__(self,n):
        self.run(n)
    def run(self,name):
            path = "./sentiments/"
            print path
            files = []
            fileTypeStr = ["Neu","Neg","Pos"]
            fileStr = ["Neutral:","Negative:","Positive:"]
            i = 0
            for type in fileTypeStr:
                try:
                    files.append(open(path + name + type + ".txt", 'r'))
                    i = i + 1
                except Exception,e:
                    print(str(e))
                    print("file " + path + name + type + ".txt failed to open")
            i = 0
            for f in files:
                print("\n" + fileStr[i])
                self.printTopTen(f)
                i = i + 1

    def printTopTen(self,file):
         list = cPickle.load(file)

         for i in range(0,10):
             try:
                 print("** "+list[i])
             except Exception,e:
                 print(str(e))
         file.close()

if __name__ == "__main__":
  a = sys.argv
  getTopTweets(a[1])
