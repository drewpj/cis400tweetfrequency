import json
#import pprint #only for fun printing
from TwitterModule import *

#names = ['@IngrahamAngle','@davidhogg111','@sleepnumber','@ATT','@Allstate','@esurance','@Bayer','@RocketMortgage','@LibertyMutual','@Arbys','@TripAdvisor','@Nestle','@hulu','@Wayfair','@FoxNews','#BoycottIngramAdverts','#boycottLauraIngraham','#FireIngraham','#FireLauraIngraham']
names = ['@sleepnumber']
#names = ['@sleepnumber','@ATT','@Allstate','@esurance','@Bayer','@RocketMortgage','@LibertyMutual','@Arbys','@TripAdvisor','@Nestle','@hulu','@Wayfair','@FoxNews','#BoycottIngramAdverts','#boycottLauraIngraham','#FireIngraham','#FireLauraIngraham']
for q in names:
    name = q[1:]
    nameFile = name + '328.json'
    file = open(nameFile,'r')

    #loads decodes json objects into dictionary
    largeFile = json.load(file)


    print("successfully opened file " + q)#successfulyl reads in the file
    print(type(largeFile)) #the type of the file. inexplicably it's a dict. It should be a list?


    '''
    Prints the contents of the file. Use with caution.
    '''
    #entire dictionary
    #print json.dumps(largeFile, indent=1)

    #length of the dictionary
    print(len(largeFile))
    keys = largeFile.keys()
    print(keys)
    print(keys[666])
    print(largeFile[keys[1]]['created_at'])
    #the keys (twitter IDs) in the dictionary
    #print(largeFile.keys())

    file.close()
