lst1 = []
def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)

def quick_sort_helper(lst, start, end):
    if start < end:
        lst1.append(1)
        pivot = partition(lst, start, end)
        quick_sort_helper(lst, start, pivot - 1)
        quick_sort_helper(lst, pivot + 1, end)


def partition(lst, start, end):
    counter = 0
    x = lst[end]
    i = start - 1
    for j in range(start, end):
        counter += 1
        if lst[j] <= x:
            i += 1
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            counter += 1

    temp = lst[i+1]
    lst[i+1] = lst[end]
    lst[end] = temp

    lst1.append(counter)

    return i+1


lst = [0, 1, 2, 2, 3, 5, 5, 6, 7, 9]
quick_sort(lst)
print(lst, sum(lst1))


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        lst1.append(1)
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first, splitpoint - 1)
        quickSortHelper(alist,splitpoint + 1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
           lst1.append(1)

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
           lst1.append(1)

       if rightmark < leftmark:
           done = True


       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

       lst1.append(1)
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp



   return rightmark

alist = [9, 7, 6, 5, 5, 3, 2, 2, 1, 0]
quickSort(alist)
print(alist)
print(sum(lst1))


counter = 0
def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )

def _quicksort( aList, first, last ):
    if first < last:
        pivot = partition( aList, first, last )
        _quicksort( aList, first, pivot - 1 )
        _quicksort( aList, pivot + 1, last )


def partition( aList, first, last ) :
    for i in range( first, last ):
        global counter
        counter += 1
        if aList[i] <= aList[last]:
            global counter
            counter += 1
            swap( aList, i, first )
            first += 1
    swap( aList, first, last )
    return first


def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]

alist = [9, 7, 6, 5, 5, 3, 2, 2, 1, 0]
quicksort(alist)
print(alist)
