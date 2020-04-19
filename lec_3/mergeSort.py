def mergeSort(A, f, l):
    if f == l :
        return A[0]
    else:
        m = (l - f) // 2
        L  = mergeSort(A, f, m)
        R  = mergeSort(A, m+1, l)
        A = merge(A, L, R)
        return A

def merge(A, L, R):
    for i in range(len(A)):
        if L[i]<R[i]:
            A[i] = L[i]
        else:
            A[i] = R[i]
        return A
    

arr = [2, 4 ,1, 0]
arr = mergeSort(arr, 0, len(arr))
print(arr)
