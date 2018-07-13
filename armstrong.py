x= int(input("enter any number"))
for i in range(x):
      num=i
      result=0
      n=len(str(i))
      while(i!=0):
          digit=i%10
          result=result+digit**n
          i=i//10
if (num==result):
        print(num)