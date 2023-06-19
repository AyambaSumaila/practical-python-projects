product="iphone and android phones"
lett_d={}
for c in product:
    if c not in lett_d:
        lett_d[c]=0
    lett_d[c] =lett_d[c]+1
keys=list(lett_d.keys())

max_value=0
for key in keys:
    if lett_d[key]>lett_d[max_value]:
        max_value=key
print(max_value)
