def insertSort(A):
    for j in range(1, len(A)):

        key = A[j]
        position = j - 1
        while position>=0:
            if key % 2 == 0:
                if A[position] % 2 != 0 or (A[position] % 2 == 0 and A[position] > key):
                    A[position+1] = A[position]
                    position = position - 1
                else:
                #elif A[position] == key or (A[position] % 2 == 0 and A[position] < key):
                    break
                A[position + 1] = key


            elif key % 2 != 0:
                if A[position] % 2 == 0 or A[position] == key or A[position] > key:
                    break
                if A[position] < key:
                    A[position + 1] = A[position]
                    position = position -1
                A[position + 1] = key

A = [30, 19, 9, 15, 55, 24, 3, 78, 46, 41]
B = [0, 3, 4, 5,7 ,8, 9, 8 ,1 ,2]
insertSort(A)
insertSort(B)
print(B)
print(A)
