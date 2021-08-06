import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "jsXVq4F0pHnKg5XTlczKZXXSo"
csecret = "K2Cd3VGHuTmQzwXi8rfC4OEnpwcwRR7b77zFyhkETIfex597xz"
atoken = "1415803093313376263-pAJm8rSmP4nZauHe7GUuu2gDkNH4rx"
asecret = "cmBzYumPDLczABGyTE00QT6xE7BNzkschFS3za2twkT2b"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:ZlatanIbra11@localhost:5984/') 
try:
    db = server.create('twitter4')
except:
    db = server['twitter4']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-79.48,-2.99,-78.52,-2.04])  

#twitterStream.filter(track=['Olympics','Team USA'])
