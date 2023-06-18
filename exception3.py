try:
    number=int(input("please enter a positive number="))
    if number<0:
         raise TypeError("-----------------")
    p=number*number
except TypeError:
     print("negative")
except ValueError:
    print("I told you that just enter a positive number ")
    try:
        number=int(input("please enter a (positive positive positive) number="))
        p=number*number
    except ValueError:
            print("just positive positive positive positive ")
            number=int(input("please enter a (positive positive positive positive) number="))
            p=number*number
finally:
    print(number)
