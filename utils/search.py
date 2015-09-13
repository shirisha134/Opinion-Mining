from auth import access
import json
from mongo import save_to_mongo
twitter_api=access()

def twitter_search(twitter_api,q,max_results=200,**kw):
    search_results = twitter_api.search.tweets(q=q,count=100,**kw)
    statuses=search_results['statuses']
    max_results=min(1500,max_results)
    for i in range(15):
        try:
            next_results=search_results['search_metadata']['next_results']
        except KeyError,e:
            print "Unexpected error:", sys.exc_info()[0] 
            break
        kwargs=dict([kv.split('=')for kv in next_results[1:].split('&')])
        search_results=twitter_api.search.tweets(**kwargs)
        statuses += search_results['statuses']
        if len(statuses)>max_results:
            break
    return statuses


# Input query
q='modi'
results=twitter_search(twitter_api,q,max_results=200)
#save_to_mongo(results,'input_tweets',q)
print json.dumps(results[0],indent=2)


            

