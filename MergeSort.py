counter = 0
def _merge_sort(A):
    global counter
    if len(A)>1:
        q = len(A)//2
        left_array = A[:q]
        right_array = A[q:]

        _merge_sort(left_array)
        _merge_sort(right_array)

        i, k , j = 0, 0, 0
        while i < len(left_array) and j < len(right_array):
            counter += 1
            if left_array[i] < right_array[j]:
                A[k] = left_array[i]
                i = i + 1
            else:
                A[k] = right_array[j]
                j = j + 1
            k=k+1

        while i < len(left_array):
            counter += 1
            A[k] = left_array[i]
            i = i + 1
            k = k + 1

        while j < len(right_array):
            counter += 1
            A[k] = right_array[j]
            j = j + 1
            k = k + 1

def merge_sort(alist):
    _merge_sort(alist)
    global counter
    count_merge = counter
    counter = 0
    return alist, count_merge

lst = [0,1,2,3,4,5,6,7,8,10]
print(merge_sort(lst))

lst1 = [10, 9, 8, 7, 6,5,4,3,2,1]
print(merge_sort(lst1))