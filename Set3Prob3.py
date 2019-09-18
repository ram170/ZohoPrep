n=input()
f=0
b=len(n)-1
for i in range(0,len(n)):
  for j in range(0,len(n)):
    if(j==f or j==b):
        print(n[j],end="")
    else:
        print(end=" ")
  print("")        
  f+=1        
  b-=1        
