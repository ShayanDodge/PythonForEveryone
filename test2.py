infile=open("word.txt","r")
outfile=open('out.txt','w')
line=infile.readline()
line=line.strip()
line=line.strip(',?:')
words=line.split()
lines=[]
while line:
    lines.append(line)
    line=infile.readline()
    line=line.strip()
print(words)