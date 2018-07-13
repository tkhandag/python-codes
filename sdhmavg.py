l=[10,20,30,40,59]
info={}
def hmean(x):
    i=[(1/x) for v in x]
    s=sum(i)
    n=len(x)
    return (n/s) 
def avg(x):
    return sum(x)/len(x)
def gmean(x):
    m=1
    for v in x:
       m*=v
    return m**(1/len(x))
def means(x):
   am=avg(x)
   gm=gmean(x)
   hm= hmean(x)
   return (am,gm,hm)
print(means(l))