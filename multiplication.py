def multiply(value,factor):
    for i in range(len(value)):
        value[i]=factor*value[i]
    return value
value=[i for i in range(100000)]        
print(multiply(value,5))