# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-16 12:19:17
#  * @modify date 2020-04-16 12:19:17
#  * @desc [description]
#  */

def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i]>key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

arr = [5, 3, 2, 4 ,1]
insertion_sort(arr)
print(arr)
