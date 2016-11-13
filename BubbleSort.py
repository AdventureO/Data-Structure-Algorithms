def bubbleSort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst
b = [1, 3, 5, 4, 9, 3, 11, 2]
bubbleSort(b)
print(b)