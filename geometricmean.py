l=[10,20,30,49,59]
def gmean(x):
    m=1
    for v in x:
        m*=v
        return m**(1/len(x))
geo=gmean(l)
print("GEomatric mean",geo)    