def sort(list):
    for i in range(4):
        min = i
        for j in range(i, 5):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp


list = [5, 38, 1, 29, 94]
sort(list)
print(list)