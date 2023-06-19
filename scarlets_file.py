file=open('sumaila.txt', 'r')
txt=file.read()
t_count=0
to_count=0
for c in txt:
    if c=='t':
        t_count +=1
    elif c=='to':
        to_count +=1
print('t: '+str(t_count)+ ' occurences in file sumaila.txt')

print('to: '+str(to_count) + ' occurences in file sumaila ')