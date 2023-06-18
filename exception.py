try:
    list=[1,2,3,4,5,6,7,0]
    index=int(input("please enter a index="))
    a=1/list[index]
except ValueError as shayan:
    print("please enter another input (int)",str(shayan))
except ZeroDivisionError:
    print("please enter another input (inf)")
except IndexError:
    print("please enter another input ")
else:
    print(a)
finally:
    print(list)