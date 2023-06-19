infile=open('word.txt','r')
uniquewords=set()

for line in infile:
    line=line.strip()
    line=line.strip("\"?.,")
    words=line.split()
    for i in range(len(words)):
        words[i]=words[i].strip()
        words[i]=words[i].strip("\"?.,")
        uniquewords.add(words[i])
        # print(words[i])
print(len(uniquewords))    

infile.close()
