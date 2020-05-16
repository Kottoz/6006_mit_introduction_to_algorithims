# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-05-16 16:39:32
#  * @modify date 2020-05-16 16:39:32
#  * @desc [description]
#  */
def quickSort(lst):
    quick_list_helper(lst, 0, len(lst)-1)


def quick_list_helper(lst, first, last):
    if first < last:
        split_point = partitioning(lst, first, last)
        quick_list_helper(lst, 0, split_point-1)
        quick_list_helper(lst, split_point+1, last)

def partitioning():
     
