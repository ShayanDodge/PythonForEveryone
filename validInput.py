def input_valid(max):
    result=int(input("Enter a value between 0 and" + str(max)+  ": " ))
    while result<0 or result>max:
       print("Error")
       result=int(input("Enter a value between 0 and" + str(max)+  ": " ))
    return result

h=input_valid(23)
m=input_valid(59)
print(h,m)
