name=['amar', 'amala',' givi',
      'mainish']
newnames=[]
for x in name:
    y=x.strip()
    fc=y[0].upper()
    rc=y[1:].lower()
    n=fc+rc
    newnames.append(n)
print(newnames)    