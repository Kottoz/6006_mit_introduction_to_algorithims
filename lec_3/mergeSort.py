def mergeSort(A):
    mid = (len(A))//2
    if len(A) > 1:
        L = A[:mid]
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        i = 0 
        j = 0 
        k = 0 
        while i < len(L) and j < len(R):
            if  L[i] < R[j]:
                A[k]  = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
             A[k]  = L[i]
             i += 1
             k += 1
        while j < len(R):
             A[k]  = R[j]
             j += 1
             k += 1

#def merge(A, p, q, r):
    


arr = [2, 4 ,1, 10, 13, 0, 5]
mergeSort(arr)
print(arr)