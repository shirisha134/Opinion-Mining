import mongo
import re,sys,string
from mongo import load_from_mongo
import nltk

# prepare list of sentiment words
senti_file='affin.txt'


def sentiment_dict(senti_file):
    with open (senti_file,'r') as f:
        scores={}
        for line in f:
            term,score=line.split('\t')
            scores[term]=float(score)
    return scores
sentiment=sentiment_dict(senti_file)



###delete after completion of negative scoring
##with open ('neg_words.txt','r') as d:
##    for line in d:
##        sentiment[line]=0
##print 'length of pos + neg words'
##print len(sentiment)

# Abbrivations list
def  abbrivation_list():
    projection={'_id':False}
    abbrivations_dict={}
    res=load_from_mongo('abbrivations','list',projection=projection)
    for i in res:
        for key in i.keys():
            key=str(key)
            i[key]=str(i[key])
            abbrivations_dict[key]=i[key]
    return abbrivations_dict
            
        
abb_list=abbrivation_list()

#stopwords list
stopwords_file='stopwords.txt'
stop_lis=[]
def stopwords_list(filename):
    with open(filename,'r') as f:
        for line in f:
            line=line.replace('\n','')
            stop_lis.append(line)
stopwords_list(stopwords_file)

#Stopwords remover

def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not \
                     in stop_lis])
    return text

#Sentiment calculation

def sentiment_of_tweet(text,abb_list,sentiment):
   
    score=0.0
    accum_term=dict()
    negated=False
    term_count={}
    term_list=[]
    actual_tweet =text['text'].encode('utf-8')
    tweet =text['text'].encode('utf-8')
    regex = re.compile( r"not\b" )
    if regex.search(tweet):
        negated = True
        tweet = re.sub( r"not\b", "", tweet)
        
    #Preprocessing may increase accuracy
    #Removing urls,usernames
        
    tweet_id=text['_id']
    tweet = re.sub(r"(?:\@|https?\://)\S+", "", tweet)
    
    #Removing digits
    tweet = re.sub( r"\b\d+\b", "", tweet )
    tweet = tweet.strip().lower()
    word_list = tweet.split()
    
    # Replacing Abbrivations
    for word in word_list:
        if str(word) in sentiment.keys():
            score=score+sentiment[word]
            word_list.remove(word)
            
        elif str(word) in abb_list.keys():
            word=abb_list[word]
    
    tweet=' '.join(word for word in word_list)        
    #Removing stopwords
    tweet=remove_stopwords(tweet)
    tokens=nltk.word_tokenize(tweet)
    tags=nltk.pos_tag(tokens)
    
    #word_list = tweet.split()
   
    for word,tag in tags:
            
            
            if word in sentiment.keys():
                
                score=score +float(sentiment[word])
            else:
                score=score
                accum_term[word]=[]
                term_list.append(word)
                if word in term_count.keys():
                    term_count[word]=term_count[word]+1
                else:
                    if tag in ['NN','IN','JJ','JJR','JJS','NNS','VB','MD','POS','RB','RBR','RBS','UH','VBD','VBG','VBN','VBP','VBZ','WDT','WP','WP$','WRB']:
                        term_count[word]=1
    for word in term_list:
        accum_term[word].append(score)
        
    if not negated:
        score=score
    else:
        score = -score
        
        
    
    add_to_senti_file={}
    
    for key in accum_term.keys():
        num_pos=0
        num_neg =0
        adjusted_score=0
        term_value=0
        total_sum =0
        for score in accum_term[key]:
            total_sum = total_sum + score
        term_value = (total_sum)/len(accum_term[key])
        term_value=int(term_value)
        add_to_senti_file[key]=term_value
    #add to new words to database or file
    with open ('new_words.txt','w') as f:
        for key,value in add_to_senti_file.items():
            f.write(key+'\t'+str(value)+'\n')
            #f.write('\t'.join(tupl))

    
    
    return score,actual_tweet,tweet_id
   
    
res=mongo.load_from_mongo('input','data')
for i in res:
    a,b,c= sentiment_of_tweet(i,abb_list,sentiment)
    g={}
    g['_id']= c
    g['text'] = b
    g['sentiment'] = a
    mongo.save_to_mongo(g,'output_final','with_ourscores')
