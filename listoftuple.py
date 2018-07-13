name=['amar', 'amala',' givi',
      'mainish']
age=[30,40,50,23]
sex=['M','F','F','M']
info=[]
i=0
for x in name:
    a=age[i]
    s=sex[i]
    rec=(x,a,s)
    info.append(rec)
    i=i+1
print(info)    