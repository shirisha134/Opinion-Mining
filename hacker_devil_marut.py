from collections import Counter
lst=map(int,raw_input().split())
q=input()
sum1=0
sum2=0
while(q>0):
    q=q-1
    str1=raw_input()
    str2=raw_input()
    cnt1=Counter()
    cnt2=Counter()
    for w in str1:
        cnt1[w]+=1
    for w in str2:
        cnt2[w]+=1
    temp=cnt1
    cnt1=cnt1-cnt2
    cnt2=cnt2-temp

    for w,v in cnt1.items():
        sum1=sum1+(lst[ord(w)-97]*v)

    for w,v in cnt2.items():
        sum2=sum2+(lst[ord(w)-97]*v)
if sum1- sum2 >0:
    print "Marut"
if sum1-sum2<0:
    print "Devil"
else:
    print "Draw"
        
