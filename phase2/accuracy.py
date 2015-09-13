from __future__ import division
##True class A (TA) - correctly classified into class A
##False class A (FA) - incorrectly classified into class A
##True class B (TB) - correctly classified into class B
##False class B (FB) - incorrectly classified into class B
from mongo import load_from_mongo
from pylab import *

#estimated=load_from_mongo('input','data')
observed_outscores=load_from_mongo('output_final','without_scores')

TA=0
FA=0
TB=0
FB=0
labels = 'positive','negative'


for i in observed_outscores:
    tweet_id=i['_id']
    #print 'id',tweet_id
    senti_ob=i['sentiment']
    #print senti_ob
    senti=load_from_mongo('input','data',criteria={'_id':tweet_id},projection={'_id':0,'sentiment':1})
    senti_es = str(senti[0].values()[0])
    #print senti_es
    
    #print senti_es
    if senti_ob>0 and senti_es=='positive':
        #print 'positive'
        TA =TA+1
    #if senti_ob ==0 and senti_es=='neutral':
        #TA =TA+1
    if senti_ob <0 and senti_es =='negative':
        TB =TB +1
    if senti_ob >0 and senti_es == 'negative':
        FA =FA +1
    if senti_ob <0 and senti_es == 'positive':
        FB = FB +1
        

print TA
print TB
print FB
print FA
pos_percent=((TA+FA)/(TA+TB+FA+FB))*100
neg_percent=((FA+FB)/(TA+TB+FA+FB))*100
fracs=[pos_percent,neg_percent]
explode = (0,0.05)
pie(fracs,explode = explode,labels = labels,autopct='%1.1f%%',shadow = True,startangle=90)
title('positive and negative percents', bbox={'facecolor':'0.9', 'pad':5})


precision=(TA/(TA+FA))
recall=(TA/(TA+FB))
accuracy=((TA+TB)/(TA+TB+FA+FB))
f_measure=2*((precision*recall)/(precision+recall))


print 'precision -----%5f' %precision
print 'recall --------%5f' %recall
print 'accuracy-------%5f' %accuracy
print 'f_measure-------',f_measure

show()
 
