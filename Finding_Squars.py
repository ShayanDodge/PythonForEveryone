import math
sq=0
sq2=0

for i in range(1,101):
    if i<11:
        sq=i*i+sq

for i in range(100,0,-1):
    if math.sqrt(i)==round(math.sqrt(i)):
        sq2=i+sq2
  
squres=0
tedad=0
i=0

while i**2<101:
    squres=squres+i**2
    tedad=tedad+1
    i=i+1

print("sqr=",squres)
print("tedad",tedad)     
print(sq2,sq) 