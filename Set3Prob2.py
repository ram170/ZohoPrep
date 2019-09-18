l=[int(x) for x in input().split(',')]
o=[]
e=[]
for i in range(0,len(l)):
    if(i%2==0):
        o.append(l[i])
    else:
        e.append(l[i])
o.sort()
o.reverse()
e.sort()
j=k=0
for i in range(0,len(l)):
    if(i%2==0):
        print(o[j],end=" ")
        j+=1
    else:
        print(e[k],end=" ")
        k+=1
        
