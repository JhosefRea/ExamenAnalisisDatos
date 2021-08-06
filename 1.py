import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "777"
csecret = "K00"
atoken = "x1"
asecret = "c0"
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
server = couchdb.Server('1') 
try:
    db = server.create('twitter4')
except:
    db = server['twitter4']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-79.48,-2.99,-78.52,-2.04])  

#twitterStream.filter(track=['Olympics','Team USA'])
