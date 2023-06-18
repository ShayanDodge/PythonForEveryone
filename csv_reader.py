from csv import writer

outfile=open("CSV.csv","w", newline='')
table=writer(outfile)

table.writerow(["a","b","c"])
table.writerow(["a","b","c"])
table.writerow(["a","b","c"])

outfile.close()