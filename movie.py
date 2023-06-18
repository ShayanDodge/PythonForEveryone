from csv import reader
infile=open("CSV.csv","r")
csvreader=reader(infile)
i=0
for row in csvreader:
    if i>0:
        if int(row[1])<2000 and int(row[1])>=1990:
           print(row[0])
    i=i+1

