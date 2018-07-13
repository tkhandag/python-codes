a=input()
b=input()
c=input()
big=0
if a>b:
    if a>c:
       big=a 
    else:
        big=c
elif b>c:
    big=b
else:
  big =c
print("biggest is",big)        
