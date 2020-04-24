# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-24 07:23:29
#  * @modify date 2020-04-24 07:23:29
#  * @desc [description]
#  */

def max_heapfy(A, i):
    left_child = (2*i) +1
    right_child = (2*i) + 2

    if left_child < len(A) and A[left_child] > A[i]  :
        largest = left_child
    else:
        largest = i

    if right_child < len(A) and A[right_child] > A[largest] :
        largest = right_child

    if largest != i:
        temp = A[i]
        A[i] = A[largest]  
        A[largest] = temp
        max_heapfy(A, largest)

def build_max_heap(A):
    heap_size = len(A)
    for i in range((heap_size//2) , -1, -1):
        max_heapfy(A, i)

a = [4, 1, 3, 2, 16, 9 , 10, 14, 8, 7]
build_max_heap(a)
print(a)
     


