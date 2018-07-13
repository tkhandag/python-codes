t=int(input("enter t"))
while(t!=0):
    s=input("enter string")
    k=[]
    m=0
    for i in s:
        if i=='f':
          k.append(i)
          continue;
        if i=='c':
           k.append(i)
           continue;
        if i=='h':
            k.append(i)
            continue;
        if i=='e':
           k.append(i)
           continue;
        if 'chef'==str(k.sort()):
            m=m+1
    print("lovely ",m)        