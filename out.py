file=open("C:/Users/Shayan/Desktop/a.txt", 'r')
line = file.readline()
print(line)
#value = float(line)
while line:
	print(line)
	line = file.readline()
#value = float(line)
