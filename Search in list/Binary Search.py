pos = -1
num = int(input('Enter a Number: '))
n = int(input('Enter Number That You Need To Find Between 1 and Previously Entered Number: '))
list = []
for i in range(1, num + 1):
    list.append(i)


def search(lst, n):
    l = 0
    u = len(list) - 1
    while l <= u:
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid
            else:
                u = mid


if search(list, n):
    print('Found at', pos + 1)
else:
    print('Not Found')