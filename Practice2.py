# Check if the user is eligible to vote
age=int(input('age='))
if age<18:
    print('User is not eligible to vote')
else:
    print('User is eligible to vote')