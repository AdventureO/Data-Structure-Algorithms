def selectionSort(lst):
  for i in range( len(lst) ):
    least = i
    for k in range( i + 1 , len(lst) ):
      if lst[k] < lst[least]:
        least = k

    temp = lst[least]
    lst[least] = lst[i]
    lst[i] = temp
  return lst

b = [1, 3, 5, 4, 9, 3, 11, 2]
selectionSort(b)
print(b)