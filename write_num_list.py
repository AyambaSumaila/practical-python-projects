#This program saves a list of numbers

def main():
    number=[1, 2, 3, 4, 4, 5, 7]
    outfile=open('number.txt', 'w')
    for item in number:
        outfile.write('numberlist.txt', 'w')
        for item in number:
            if item%2==0:
                
                outfile.write(str(item)+'\n')
            
            outfile.close()
main()
