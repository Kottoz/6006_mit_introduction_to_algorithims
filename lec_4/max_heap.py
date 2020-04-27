# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-24 07:23:29
#  * @modify date 2020-04-24 07:23:29
#  * @desc [description]
#  */
def max_heapfy(A, n, i):
    n = len(A)
    left_child = (2*i) +1
    right_child = (2*i) + 2
    largest = i

    if left_child < len(A) and A[left_child] > A[i]  :
        largest = left_child        

    if right_child < len(A) and A[right_child] > A[largest] :
        largest = right_child

    if largest != i:
        A[i], A[largest] = A[largest], A[i]  
        max_heapfy(A, n, largest)

def build_max_heap(A):
    heap_size = len(A)
    for i in range((heap_size//2) , -1, -1):
        max_heapfy(A, heap_size, i)

def heap_sort(A):
    n = len(A)
    build_max_heap(A)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapfy(A, i, 0)

a = [3, 1, 5, 12, 2, 4 , 6, 4, 7]
heap_sort(a) 
print(a)
     


