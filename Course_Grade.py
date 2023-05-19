def main():
    grade=input('grade = ')
    sum=0
    i=0
    while grade in "AA+A-BB+B-CC+C-DD+DD-F":
        number=gradeTonumber(grade)
        sum=sum+number
        i=i+1
        grade=input('grade = ')
    average=sum/i
    average_grade=numberTograde(average)
    return print(sum,average,average_grade)
    
def gradeTonumber(grade):
    first=grade[0]
    
    if   first=='A': result = 4
    elif first=='B': result = 3
    elif first=='C': result = 2
    elif first=='D': result = 1
    elif first=='F': result = 0
    
    if len(grade)>1:
        second=grade[1]
        if second=='+': result = result + 0.3
        elif second=='-': result = result - 0.3
        
    return result

def numberTograde(number):
    if   number < 0.35: return 'F'
    elif number < 0.85: return 'D-'
    elif number < 1.15: return 'D'
    elif number < 1.50: return 'D+'
    elif number < 1.85: return 'C-'
    elif number < 2.15: return 'C'
    elif number < 2.50: return 'C+'
    elif number < 2.85: return 'B-'
    elif number < 3.15: return 'B'
    elif number < 3.50: return 'B+'
    elif number < 3.85: return 'A-'
    elif number < 4.15: return 'A'
    elif number < 4.30: return 'A+'
 
main()   