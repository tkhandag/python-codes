prid=['P1','P2', 'P3']
pname=['TV', 'LAPTOP','MOBILE']
brand=['HCL' , 'SUMSANG' , 'LENOVO']
price=[2000,40000,3000]
pinfo={}
i=0
for x in prid:
    b=brand[i]
    n=pname[i]
    p=price[i]
    info=(b,n,p)
    pinfo[x]=info
    i=i+1
print(pinfo)    