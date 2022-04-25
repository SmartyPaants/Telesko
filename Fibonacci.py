def fib(n):
    a, b = 0, 1
    if n <= 0:
        print('Not Valid')
    else:
        if n == 1:
            print(a)
        else:
            print(a)
            print()
            print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print()
        print(c)

fib(int(input('Enter a Number: ')))