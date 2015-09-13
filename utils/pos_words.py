list_pos={}
with open('C:\Users\user\Desktop\sh_neg.txt') as f:
    count = 0
    for line in f:
        count +=1
        #print "line is :"
        if count > 4747:
            print count
        line=line.rstrip('\t')
        #print line
        
        word,score=line.split('\t')
        
        list_pos[word]=score
#print len(list_pos)
        
