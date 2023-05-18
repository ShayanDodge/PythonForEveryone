def main():
    number=input_valid(1000)
    print(number_to_word(number))
    
def input_valid(max):
    result=int(input("Enter a value between 0 and " + str(max)+  ": " ))
    while result<0 or result>max:
        print("Error")
        result=int(input("Enter a value between 0 and" + str(max)+  ": " ))
    return result

def number_to_word(digit):
    part=digit
    word=''
    
    if part>=100:
        word = digit_name(part//100)+' hundred'
        part=part%100
        
    if part>=20:
        word=word+' '+digit_ty(part//10)
        part=part%10
    elif part>=10:
         word=word+' '+digit_teen(part)
         part=part%10       
        
    if part>0:
        word=word+' '+digit_name(part)
    return word
        
def digit_name(digit):
    if digit==1: return 'one'
    if digit==2: return 'two'
    if digit==3: return 'three'
    if digit==4: return 'four'
    if digit==5: return 'five'
    if digit==6: return 'six'
    if digit==7: return 'seven'
    if digit==8: return 'eight'
    if digit==9: return 'nine'
    return ''

def digit_teen(digit):
    if digit==10: return 'ten'
    if digit==11: return 'eleven'
    if digit==12: return 'twelve'
    if digit==13: return 'thirteen'
    if digit==14: return 'fourteen'
    if digit==15: return 'fifteen'
    if digit==16: return 'sixteen'
    if digit==17: return 'seventeen'
    if digit==18: return 'eighteen'
    if digit==19: return 'nineteen'
    return ''

def digit_ty(digit):
    if digit==2: return 'twenty'
    if digit==3: return 'thirty'
    if digit==4: return 'forty'
    if digit==5: return 'fifty'
    if digit==6: return 'sixty'
    if digit==7: return 'seventy'
    if digit==8: return 'eighty'
    if digit==9: return 'ninety'
    return ''

main()