a = int(input('Enter a Number: '))
if a % 2 == 0:
    print('Number is Even')
    if a < 50:
        print('Number is Less Than 50')
    else:
        print('Number is Greater Than 50')
else:
    print('Number is Odd')