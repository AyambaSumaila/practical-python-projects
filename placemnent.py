placement="Beaches are cool places to visit in spring however the Mackinow Bridge is near.Most people visit Mackinow later:"
        
d={}
for c in placement:
    if c not in d:
        d[c]=0
    d[c] +=1
    
keys=list(d.keys())
min_value=keys[0]
for key in keys:
    if d[key]<d[min_value]:
        min_value=key
print(min_value)
    