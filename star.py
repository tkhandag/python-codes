pattern=int (input())
for i in range(pattern , 0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()    