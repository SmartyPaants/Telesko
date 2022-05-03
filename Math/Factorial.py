def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    print(f)

x = int(input('Enter Number For Factorial: '))
factorial(x)