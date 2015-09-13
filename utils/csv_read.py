import csv
from mongo import save_to_mongo
from mongo import load_from_mongo
fp = open( 'E:\\7th_Sem\\senti\\sanders-twitter-0.2\\sanders-twitter-0.2\\full-corpus.csv', 'r' )
reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
tweets = []
count=0
for row in reader:
    count += 1
    g={}
    g['category']=row[0]
    g['sentiment']=row[1]
    g['_id']=count
    g['created_at']=row[3]
    g['text']=row[4]
    save_to_mongo(g,'input','data')





    
