def person(name, age):  # Positional Arguments
    print('Name is', name)
    print('Age is', age)


person('Siddhant', 12)
print()


def person(name, age):  # Keyword Arguments
    print('Name is', name)
    print('Age is', age)


person(age=12, name='Siddhant')
print()


def person(name, age=30):  # Default Arguments
    print('Name is', name)
    print('Age is', age)


person('Sddhant')
print()


def sum(*b):  # Variable Length Arguments
    c = 0
    for i in b:
        c += i
    print(c)


sum(5, 6, 34, 78)
print()

def person(name, **data):
    print('Name is', name)
    for i, j in data.items():
        print(i, j)


person('Siddhant', Age = 12, City = 'Eindhoven', Number = 1234567890)