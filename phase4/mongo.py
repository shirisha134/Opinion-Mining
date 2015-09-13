import json
import pymongo
#from accessing_twitter import oauth_login
import sys
import time


def save_to_mongo(data,mongo_db,mongo_db_coll,**mongo_conn_kw):
    client = pymongo.MongoClient('192.168.33.6',27017)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    try:
        return coll.insert(data)
    except:
        print "unexpected error",sys.exc_info()[0]
        
def load_from_mongo(mongo_db,mongo_db_coll,
                    return_cursor=False,criteria=None,projection=None,
                    **mongo_conn_kw):
    client = pymongo.MongoClient('192.168.33.6',27017)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    if criteria is None:
        criteria={}
    if projection is None:
        cursor = coll.find(criteria)
    else:
        cursor = coll.find(criteria,projection)
    if return_cursor:
        return cursor
    else:
        return [item for item in cursor]

def del_from_mongo(data,mongo_db,mongo_db_coll,**mongo_conn_kw):
    client = pymongo.MongoClient('192.168.33.45',27017)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    try:
        return coll.remove(data)
    except:
        print "unexpected error",sys.exc_info()[0]
        
