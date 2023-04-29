Rate1=0.10
Rate2=0.25
singleIncome=32000
marriedIncome=64000

income=float(input('income='))
maritalStatus=input('s or m =')

tax1=0.0

if maritalStatus=='s':
    if income<=singleIncome:
        tax=Rate1*singleIncome
    else:
        tax=Rate2*singleIncome+3200
else:
    if income<=marriedIncome:
        tax=Rate1*marriedIncome
    else:
        tax=Rate2*marriedIncome+6400

print('Tax is %10.2f' %tax)
