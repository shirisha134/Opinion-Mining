import sys
import time
from urllib2 import URLError
from httplib import BadStatusLine
import json
import twitter
from auth import access
def make_twitter_request(twitter_api_func,max_errors=10,*args,**kw):
    def handle_twitter_http_error(e,wait_period=2,
                                  sleep_when_rate_limited = True):
        if wait_period > 3600:
            print >> sys.stderr,'to many requsets'
            raise e
        if e.e.code == 401:
            print >> sys.stderr, "encountered 401 error(not authorized)"
            return None
        elif e.e.code == 404:
            print >> sys.stderr, 'encountered 404 Error (not found)'
            return None
        elif e.e.code == 429:
            print>> sys.stderr,'encounterd 429 error(rate limit exceeded)'
            if sleep_when_rate_limited:
                print >>sys.stderr,'retrying in 15 mins....zzzzzz....'
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print >> sys.stderr,'Zzzz..awake now try again'
                return 2
            else:
                raise e
        elif e.e.code in (500,502,503,504):
            print >> sys.stderr,'encountered %i error,retrying in %i seconds' %\
                     (e.e.code,wait_period)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e
    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitter_api_func(*args,**kw)
        except twitter.api.TwitterHTTPError,e:
            error_count = 0
            wait_period = handle_twitter_http_error(e,wait_period)
            if wait_period is None:
                return
        except URLError,e:
            error_count +=1
            print >> sys.stderr,'URLERROR encountered'
            if error_count >max_errors:
                print >> sys.stderr,'Too many consequtive error ...bailing now'
                raise
        except BadStatusLine,e:
            error_count += 1
            print>> sys.stderr,'badststusline error'
            if error_count >max_errors:
                print >> sys.stderr,'too many erroe bailing out'
                raise
twitter_api = access()
response = make_twitter_request(twitter_api.search.tweets(q='iphone',count=100))
#print json.dumps(response,indent = 2)
print 'the end'
