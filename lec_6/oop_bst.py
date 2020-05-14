# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-05-14 15:41:24
#  * @modify date 2020-05-14 15:41:24
#  * @desc [description]
#  */
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None 
        self.right_child = None

    def insert_left(self, new_object):
        if self.left_child == None:
            self.left_child = BinaryTree(new_object)
        else: 
            t = BinaryTree(new_object)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, new_object):
        if self.right_child == None:
            self.right_child = BinaryTree(new_object)
        else: 
            t = BinaryTree(new_object)
            t.right_child = self.right_child
            self.right_child = t