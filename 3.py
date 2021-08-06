import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb



#variables del destino COUCHDB

URL = 'http://admin:ZlatanIbra11@localhost:5984'
print(URL)

try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)
HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

#variables del origen

CLIENT = MongoClient()

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)


DBS=['examen']

#creación de la base en couchdb destino
try:
    dbc=server.create('examen1')
except:
    dbc=server['mongocouch']
    

#insertar datos
for db in DBS:
    if db not in ('admin', 'local','config'):  #q ingrese a la BD q no sea estas
        cols = CLIENT[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try: #61--66 formamos el json
                    
                    documents=json.loads(json_util.dumps(x))

                    documents["_id"]=str(documents["_id"]["$oid"])


                    print(documents)
                    doc=dbc.save(documents) #crea el documento "doc", insertamos el json

                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  # creating list of skipped documents for later analysis
                    continue    # continue to next document
                except Exception as e:
                    raise e