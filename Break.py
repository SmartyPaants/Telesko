a = int(input('How Many Candies Do You Want: '))
av = 100
i = 1
while i <= a:
    if i > av:
        print('Out of Stock')
        break          #Jump out of Loop
    print('Candy')
    i += 1