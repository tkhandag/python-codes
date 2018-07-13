t=int(input())
for i in range(0,t):
    a=int(input())
    b=int(input())
    count=1
    for v in range(2,a+1):
        a=a*v
        count=count+1
    if a==b:    
        print(count)
    else:
        print(1)
           