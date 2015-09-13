import requests,re
import urllib2
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
from mongo import save_to_mongo
proxy = {'http': 'http://192.168.1.103:3128'}
auth=HTTPProxyAuth('ipg_2011101','chitti   chinni')

url = "http://en.wikipedia.org/wiki/List_of_emoticons"
print url
r=requests.get(url,proxies=proxy,auth=auth)
soup = BeautifulSoup(r.content)
table = soup.find_all('table',{'class':'wikitable'})
rows = table[0].find_all('td')
for i in range(0,len(rows),2):
     a=rows[i].text.encode('utf-8')
     b=rows[i+1].text
     b = re.sub(r'\[','',b)
     b = re.sub(r'\]','',b)
     b = re.sub(r'\d','',b)
     print b
     a=a.decode('utf-8').split()
     g={}
     g['icons']= a
     g['meaning'] = b
     save_to_mongo(g,'emoticons','list')
