def Square():
    n = 1
    nums = int(input('Enter The Number of Squared Number You Want: '))
    while n <= nums:
        square = n * n
        yield square
        n += 1


Square = Square()
for i in Square:
    print(i)