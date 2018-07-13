l=[20,10.59,34]
def avg(x):
    return sum(x)/len(x)
def strdev(x):
    m=avg(x)
    ds=[(v-m)**2 for v in x]
    s=sum(ds)
    n=len(x)
    return (s/(n-1))**0.5
sd=strdev(l)
print("standard deviation",sd)