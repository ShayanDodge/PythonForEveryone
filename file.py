infile=open('text.txt','r')

for line in infile:
    line=line.rstrip()
    print(line)

# outfile=open('text2.txt','w')
# ave=0
# num=0
# total=0
# line=infile.readline()
# print("%20s"%"output",file=outfile)
# while line:
#     line=infile.readline()
#     if line=="":
#         break
#     total=total+float(line)
#     num=num+1
#     print("%20s"%line,file=outfile)
# ave=total/num
# print(20*"-",file=outfile)
# print("Total = ""%10f"%total,file=outfile)
# print("Average = ""%10f"%ave,file=outfile)

# outfile.close()
