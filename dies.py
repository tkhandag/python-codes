t=int(input())
for v in range(0,t):
    n,a,b=int(input()),int(input()),int(input())
    list=[]
    for i in range(0,n):
        list.append(int(input()))
    if(list[0]==a):
        if(list[1]==b):
            print(float(a/b))
        else:
            print(b/(list[1]*list[1]))
    else:
          print(float(list[0]/n))      
    
    