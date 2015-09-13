import twitter

''' authentication to access twitter api'''

def access():
    consumer_key='QZUgeM5o5XXldjnf0R9hH2Qeq'
    consumer_secret='sWJcua2CCUA9AuT7K0GYphY9DE5EyyBdkRNMy45Zhx9VgWDqpK'
    access_key ='2524222789-e3W62i0llIRbEZzn9yVqC6tCPGInpMsgTiplzUV'
    access_secret='a6P0ns1fiEpff7vIIR5SSXikpyO87Ly08qSCuVgmdV89T'
    my_auth = twitter.oauth.OAuth(access_key,access_secret,consumer_key,consumer_secret)
    twitter_api = twitter.Twitter(auth=my_auth)
    return twitter_api

