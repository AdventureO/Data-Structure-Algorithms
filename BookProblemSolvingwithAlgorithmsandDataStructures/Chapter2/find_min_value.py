def find_min_n(lst):
    min_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value


find_min_n([4, 6, 0, 9, 8, 5, 2, -3, 5, 8])

