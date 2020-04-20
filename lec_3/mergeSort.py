def mergeSort(A):
    print("Spliting", A)
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
    print("Merging", A)
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(arr)
print(arr)