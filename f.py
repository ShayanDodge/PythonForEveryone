def addTax(price, rate) :
	tax = price * rate / 100
	price = price + tax 
	# Has no effect outside the function.
	return tax

total = 10
tax=addTax(total, 7.5) # Does not modify total.
print(total)
print(tax)
