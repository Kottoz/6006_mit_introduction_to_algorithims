# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-05-14 14:46:55
#  * @modify date 2020-05-14 14:46:55
#  * @desc [description]
#  */
def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t)>1:
        root.insert(1, [new_branch, t, []])
    else: 
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t)>1:
        root.insert(2, [new_branch, t, []])
    else: 
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]
# 
#                        a          
#                      /    \
#                     b      c
#                    / \    /  \ 
#                  []   d  e    f
# 

t = binary_tree('a')
insert_left(t, 'b')
insert_right(t, 'c')
insert_right(get_left_child(t), 'd')
insert_right(get_right_child(t), 'f')
insert_left(get_right_child(t), 'e')


print(t)