f1=open("A:/python codes/parent.txt")
h=f1.readline()
lines=f1.readlines()
f2=open("A:/python codes/children.txt")
h2=f2.readline()
lines2=f2.readlines()
kids={}
for line in lines2:
    w=line.split(",")
    pid=w[-1].split("\n")[0]
    age=int(w[2])
    if kids.get(pid)==None:
      kids[pid]=[age]
    else:
      kids[pid].append(age)
print("kids :",kids)

parents={}
for line in lines:
    w=line.split(",")
    pid=w[0]
    pname=w[1]
    parents[pid]=pname
print("parents :",parents)
keys=kids.keys()  
results=[]
for v in keys:
    pname=parents[v]
    ages=kids[v]
    n=len(ages)
    tot=sum(ages)
    avg=tot/n
    info=(pname,age)
    results.append(info)
print(results)