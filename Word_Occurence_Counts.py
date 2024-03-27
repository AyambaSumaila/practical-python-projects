def main():
    #Prompt the user to enter a file
    filename=input('Enter the name of a file name:').strip()
    myfile=open(filename, "r")
    #opening the file
    word_counts={}
    #Dictionary to store the words
    for line in myfile:
        processLines(line.lower(), word_counts)
        
        pairs=list(word_counts.items())
        #Get pairs from the dictionary
        items=[[x, y] for (y, x) in pairs]
        items.sort()
        #Sort pairs in items
        
        for i in range(len(items) - 1, len(items) - 11, -1):
           print(items[i][1] + "\t" + str(items[i][0]))
            
def processLines(line, word_counts):
     line=replacePunctuations(line)
     words=line.split()#Get words from each line
     for word in words:
         if word in word_counts:
             word_counts[word] +=1
         else:
             word_counts[word] =1
             
#Replace puntuation in the line with a space
def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line=line.replace(ch, " ")
    return line



main()    