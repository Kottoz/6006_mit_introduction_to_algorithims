# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-24 07:23:29
#  * @modify date 2020-04-24 07:23:29
#  * @desc [description]
#  */

def max_heapfy(A, i):
    
    if i == 0 :
        left_child = 1
        right_child = 2
    else:
        left_child = 2*i
        right_child = (2*i) + 1

    if A[left_child] > A[i] and left_child < len(A):
        largest = left_child
    else:
        largest = i

    if A[right_child] > A[largest] and right_child < len(A):
        largest = right_child

    if largest != i:
        temp = A[i]
        A[i] = A[largest]  
        A[largest] = temp
        max_heapfy(A, largest)

a = [float('-inf'),8, 9, 10, 1, 3, 11]
max_heapfy(a, 1)
print(a)
     


