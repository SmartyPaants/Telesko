lst = []
a = int(input('Enter Length of List: '))
for i in range(a):
    lst.append(int(input('Enter Value: ')))


def count(list):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = count(lst)
print('There Are', even, 'Even Numbers')
print('There Are', odd, 'Odd Numbers')