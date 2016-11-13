def insertionSort(A):
    for j in range(1, len(A)):

        key = A[j]
        position = j - 1

        while position>=0 and A[position]>key:
            A[position+1] = A[position]
            position = position - 1

        A[position+1] = key


A = [1, 3, 5, 4, 9, 3, 11, 2]
insertionSort(A)
print(A)