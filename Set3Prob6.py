def rev(a,l):
    if(l!=-1):
        print(a[l],end=" ")
        return rev(a,l-1)
s=[x for x in input().split()]
rev(s,len(s)-1)
