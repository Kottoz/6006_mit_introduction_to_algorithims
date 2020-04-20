def mergeSort(A, p, r):
    q = (p+r)//2
    if p < r:
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    L = [A[i] for i in range(p, q)]
    R = [A[i] for i in range(q+1, r)]
    L.append(float('inf'))
    R.append(float('inf'))
    i = 0 
    j = 0  
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1 

    

arr = [2, 4 ,1, 0]
mergeSort(arr, 0, len(arr))
print(arr)
