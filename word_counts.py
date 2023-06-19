file=open('sumaila.txt', 'r')
txt=file.read()
x={}
for c in txt:
    if c not in x:
        x[c]=0
    x[c] +=1
print('t:' + str(x['t']) + ' occurences ')
print('s:' + str(x['s']) + ' occurences ')
print('a:' + str(x['a']) + ' occurences ')
print('b:' + str(x['b']) + ' occurences ')
print('the:' + str(x['e']) + ' occurences ')
print(',  :' + str(x[',']) + ' occurences ')