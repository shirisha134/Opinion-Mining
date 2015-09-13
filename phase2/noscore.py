import mongo
import re,sys,string

pos_words=[]
neg_words=[]
pos_filename='positive-words.txt'
neg_filename = 'neg_words.txt'
def prepare_list(filename,list_name):
    with open(filename,'r') as f:
        for line in f:
            list_name.append(line.rstrip('\n'))
    return list_name
pos_words=prepare_list(pos_filename,pos_words)
neg_words=prepare_list(neg_filename,neg_words)

stopwords_file='stopwords.txt'
stop_lis=[]


def  abbrivation_list():
    projection={'_id':False}
    abbrivations_dict={}
    res=mongo.load_from_mongo('abbrivations','list',projection=projection)
    for i in res:
        for key in i.keys():
            key=str(key)
            i[key]=str(i[key])
            abbrivations_dict[key]=i[key]
    return abbrivations_dict
            
        
abb_list=abbrivation_list()

def stopwords_list(filename):
    with open(filename,'r') as f:
        for line in f:
            line=line.replace('\n','')
            stop_lis.append(line)
stopwords_list(stopwords_file)

def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not \
                     in stopwords_list])
    return text


def sentiment(text,abb_list):
    score=0.0
    negated=False
    tweet =text['text'].encode('utf-8')
    actual_text=tweet
    regex = re.compile( r"not\b" )
    if regex.search(tweet):
        negated = True
        tweet = re.sub( r"not\b", "", tweet)
    #preprocessing may increase accuracy
    
    tweet_id=text['_id']
    tweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet)
    
    tweet = re.sub( r"\b\d+\b", "", tweet )
    tweet = tweet.strip().lower()
    word_list = tweet.split()
    for k in word_list:
        if any( k == s for s in pos_words):
            score = score +1
        elif any( k == s for s in neg_words):
            score = score -1
    if negated:
        score = -score
    return  score, actual_text,tweet_id 

res=mongo.load_from_mongo('input','data')
for i in res:
    a,b,c = sentiment(i,abb_list)
    g={}
    g['_id']=c
    g['text'] = b
    g['sentiment'] = a
    mongo.save_to_mongo(g,'output_final','without_scores')

