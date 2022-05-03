from functools import *
nums = []
a = int(input('Enter Length of List: '))
for i in range(a):
    b = int(input('Enter Value: '))
    nums.append(b)
evens = list(filter(lambda n : n % 2 == 0, nums))            #filter to filter values
doubles = list(map(lambda n : n * 2, evens))                #Apply certain opperation
sum = reduce(lambda a, b : a + b, doubles)
print('From Nums, Even Numbers Are: ', evens)
print('Evens Doubled: ', doubles)
print('Sum of All Numbers Which Have Been Doubled: ', sum)