import treenode as tn
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0  

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = tn.TreeNode(key, val)
        self.size = self.size+1
    
    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else: 
                current_node.left_child = tn.TreeNode(key, val,
                        parent=current_node)
        else: 
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else: 
                current_node.right_child = tn.TreeNode(key, val,
                        parent= current_node)


bst = BinarySearchTree()
bst.put(13, 7)
bst.put(5, 7)
bst.put(34, 7)
bst.put(14, 7)
