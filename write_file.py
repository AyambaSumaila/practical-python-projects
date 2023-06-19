my_file=open("sumaila.txt", 'w')
for num in range(13):
    square=num*num
    my_file.write(str(square))
    my_file.write('\n')
my_file.close()