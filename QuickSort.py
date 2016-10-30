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
#lst1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quick_sort(lst))
#print(quick_sort(lst1))
"""
counter = 0
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   global counter
   quick_counter = counter
   counter = 0
   return alist, quick_counter

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global counter
   pivotindex = median(alist, first, last, (first + last) // 2)
   alist[first], alist[pivotindex] = alist[pivotindex], alist[first]
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           counter += 1
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           counter += 1
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def median(a, i, j, k):
  if a[i] < a[j]:
    return j if a[j] < a[k] else k
  else:
    return i if a[i] < a[k] else k

lst = [1,2,3,4,5,6,7,8,9,10]
print(quickSort(lst))


lst1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(quickSort(lst1))
"""