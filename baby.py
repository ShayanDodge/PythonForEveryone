from csv import reader
infile=open('baby_2022.csv','r')
csvreader=reader(infile)
total_b=0
total_g=0
i=1
j=0
for row in csvreader:
    if j>0:
        total_b=float(row[2].rstrip("%"))+total_b
        total_g=float(row[4].rstrip("%"))+total_g
        if total_b>=50 and total_g>=50:
            break
        if total_b<=50:
            print(i,end='')
            print("%10s"%row[1],end="")
        else:
            print(i,end='')
            print("%10s"%" ",end="")
        if total_g<=50:
            print("%10s"%row[3],end="")
        i=i+1
        print()
    j=j+1
