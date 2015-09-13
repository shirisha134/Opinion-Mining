import requests
import urllib2
from requests.auth import HTTPProxyAuth
from bs4 import BeautifulSoup
from mongo import save_to_mongo
proxy = {'http': 'http://192.168.1.103:3128'}
auth=HTTPProxyAuth('ipg_2011101','chitti   chinni')

lis=[1,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in lis:
    url = "http://www.noslang.com/dictionary/%s/" %(i)
    print url

    r = requests.get(url, proxies=proxy, auth=auth)
    soup = BeautifulSoup(r.content)
    table = soup.find_all('table',{'width':"768"})
    tab = table[0].find_all('td',{'width':'608'})
    lst1 = tab[0].find_all('dt')
    lst2 = tab[0].find_all('dd')
    for i,j in zip(lst1,lst2):
        g={}
        g[i.text]=j.text
        save_to_mongo(g,'abbrivations','list')
    


