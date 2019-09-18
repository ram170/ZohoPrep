l=list(input())
d={}
for i in range(0,len(l)):
    c=d.keys()
    if l[i] in c:
        d[l[i]]+=1
    else:
        d[l[i]]=1
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(d)
#print(sorted(d.items(),key=lambda x:x[1]))        
