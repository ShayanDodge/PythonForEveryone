# 
initialInvestment=100
Rate=0.25
goal=200
#
year=0
balance=initialInvestment
#
while balance<goal:
    balance=balance*Rate+balance
    year=year+1
print("After %d years your balance will be %.2f $" %(year,goal))