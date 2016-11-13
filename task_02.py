def count_inversions(data, y):
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
print(count_inversions([[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
[2, 10, 8, 9, 5, 4, 3, 7, 6, 1],
[2, 4, 9, 6, 10, 7, 5, 1, 3, 8],
[3, 9, 10, 6, 7, 4, 1, 2, 5, 8],
[7, 3, 8, 6, 5, 4, 10, 1, 2, 9]], 1))