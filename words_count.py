sentence="The dog chased the rabbit into the forest but the rabbit was too quick"
words=sentence.split()
word_counts={}
for word in words:
    if word not in word_counts:
        word_counts[word]=0
    word_counts[word] +=1
print(word_counts)