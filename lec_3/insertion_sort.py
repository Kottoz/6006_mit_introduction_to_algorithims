# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-16 12:19:17
#  * @modify date 2020-04-16 12:19:17
#  * @desc [description]
#  */
#O(n^2)
def insertion_sort(A):
    for j in range(len(A)): #O(1) -- O(len(A))[O(n)]
        key = A[j]          #O(1)
        i = j - 1           #O(1)    
        while i >= 0 and A[i]>key:#O(n)  
            A[i+1] = A[i]           #O(1)
            i = i - 1           #O(1)
        A[i+1] = key            #O(1)

arr = [5, 3, 2, 4 ,1]
insertion_sort(arr)
print(arr)
