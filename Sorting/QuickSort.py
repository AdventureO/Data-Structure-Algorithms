counter1 = 0
def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)
    global counter1
    quick_counter = counter1
    counter1 = 0
    return lst, quick_counter

def _quick_sort(lst, start, end):
    if start < end:
        pivot = partition(lst, start, end)
        _quick_sort(lst, start, pivot - 1)
        _quick_sort(lst, pivot + 1, end)

def partition(lst, start, end):
    x = lst[end]
    i = start - 1
    global counter1
    for j in range(start, end):
        counter1 += 1
        if lst[j] <= x:
            i += 1
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

    temp = lst[i+1]
    lst[i+1] = lst[end]
    lst[end] = temp

    return i+1

lst = [0,1,2,3,4,5,6,7,8,10]
print(quick_sort(lst))
