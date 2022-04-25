n = int(input('Enter Length of List: '))
list = []
for i in range(n):
    element = int(input('Enter Element: '))
    list.append(element)
for num in list:
    if num % 5 == 0:
        print(num)
        break
else:
    print('Not Found')