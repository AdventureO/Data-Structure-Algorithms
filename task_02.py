def count_inversions(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = count_inversions(x[:mid])
    z = count_inversions(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result

A = [1,34,5,67,4,3,2,1,876,5433,0,-12]
#print(count_inversions(A))

def lol(data, y):
    result = []
    main_watcher = data[y]
    for k in range(len(data)):
        lst = len(data[k])*[0]
        for i in range(len(data[k])):
            lst[int(main_watcher[i]) - 1] = data[k][i]
        inversions_count = 0
        lst1 = lst
        for i in range(len(lst)):
            element = lst[i]
            for j in range(len(lst1)):
                if element > lst1[j]:
                    inversions_count += 1
            lst1 = lst[i+1:]
        result.append([k, inversions_count])
        if result.count([y, 0]) == 1 :
            result.remove([y, 0])

    result.sort(key = lambda row: row[1])

    return result

a = [[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
     [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
     [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
     [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
     [3, 2, 10, 6, 9, 1, 5, 7, 4, 8]]
b = [[2,5,3,4,1],[1,5,4,3,2]]
print(lol([[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
[2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
[2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
[3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
[7, 3, 8, 6, 5, 4, 10, 1, 2, 9]], 1))