class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key 
        self.pay_load = val
        self.left_child = left 
        self.right_child = right
        self.parent = parent
    
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not(self.left_child or self.right_child)
    
    def has_any_children(self):
        return self.left_child or self.right_child

    def replace_node_data(self, key, value, lc, rc):
        self.pay_load = value
        self.key = key
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self



