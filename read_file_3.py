my_file2=open('sumaila.txt', 'r')
line=my_file2.readlines()
print(len(line))
for i in line:
    
    print(i[:4])
    
my_file2.close()
 

