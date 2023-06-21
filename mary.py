infile=open("word.txt","r")
wordSet=set()
for line in infile:
    line=line.strip()
    line=line.strip(".,?\"")
    word=line.split()
    for i in range(len(word)):
        word[i]=word[i].strip()
        word[i]=word[i].strip(".,?\"")
        wordSet.add(word[i])
    # print(word)
print(wordSet)
print(len(wordSet))