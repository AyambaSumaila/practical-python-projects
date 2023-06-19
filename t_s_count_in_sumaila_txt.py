file=open('sumaila.txt', 'r')
txt=file.read()
x={}
x['t']=0
x['s']=0

for c in txt:
    if c=='t':
        x[c] +=1
    elif c=='s':
        x[c] +=1
print('t : ' + str(x['t']) + ' occurences')
print('s : ' + str(x['s']) + ' occurences')

        