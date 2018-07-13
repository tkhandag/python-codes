t=int(input())
while(t!=0):
    n=int(input())
    mylist=[]
    for i in range(0,n):
        n=int(input())
        mylist.append(n)
    k=mylist[0]
    for v in mylist:
        if k>v:
            k=v
    print(k)
    t-=1        