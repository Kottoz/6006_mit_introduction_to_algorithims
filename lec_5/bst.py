class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0  

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(slef, key, val):
        if self.root:
            self._put(key, val, self.root)

