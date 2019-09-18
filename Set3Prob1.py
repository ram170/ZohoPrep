s=input()
n=[]
a=[]
num=str()
f=0
for i in range(0,len(s)):
    if(i==0):
        a.append(s[i])
    elif(s[i].isnumeric()):
        if(f==0):
            num=num+s[i]
            f=1
        else:    
            num=num+s[i]
    else:
        n.append(num)
        num=str()
        f=0
        a.append(s[i])
    if(i==len(s)-1 and f==1):
        n.append(num)
#print(n,a)        
for i in range(0,len(a)):
    print(a[i]*int(n[i]),end="")
