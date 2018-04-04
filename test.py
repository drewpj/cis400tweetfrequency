import json
import pprint
from TwitterModule import *


file3 = open('esurance328.json','r')
largeFile = json.load(file3)
file3.close()


print("success")#successfulyl reads in the file

print(type(largeFile)) #the type of the file. inexplicably it's a dict. It should be a list?

'''
Prints the contents of the file. Use with caution.
'''
#print json.dumps(largeFile, indent=1)


print(len(largeFile))#length of the dictionary
print(largeFile.keys())#the keys (twitter IDs) in the dictionary
