		#MATRIX MULTIPLICATION
# Program to multiply two matrices using nested loops
print("enter no. of elements")
n=int(input())
X=[]
for x in range(0,n):
    k=int(input())
    s=int(input())
    l=int(input())
    rec=[k,s,l]
    [X].append(rec)
# 3x3 matrix
# 3x4 matrix
Y=[]
for x in range(0,n):
    p=int(input())
    r=int(input())
    q=int(input())
    reco=[p,r,q]
    [Y].append(reco)
# result is 3x4
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)