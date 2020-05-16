# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-05-16 16:39:32
#  * @modify date 2020-05-16 16:39:32
#  * @desc [description]
#  */

def quickSort(lst, first, last):
    if lst[first] < lst[last]:
        split_point = partitioning(lst, first, last)
        quickSort(lst, 0, split_point-1)
        quickSort(lst, split_point+1, last)

def exchange(n1, n2):
    temp = n1
    n1 = n2
    n2 = temp

def partitioning(lst, first, last):
    piv = lst[last]
    i = first - 1
    for j in range(len(lst)):
        if lst[j]< piv:
            i += 1
            exchange(lst[j], lst[i])
    exchange(lst[i+1], lst[last-1])
    return i+1

l = [2, 8, 7, 1, 3, 5, 6, 4]
quickSort(l, 0, len(l)-1)





