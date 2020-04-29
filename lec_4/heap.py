class heap(object):
    def __init__(self):
        self.heap_list = [0]
        self.heap_size = 0 
    def prec_up(self, i):
        while i > 0 :
            if self.heap_list[i] < self.heap_list[i//2]:
                temp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = temp 
            i = i//2 
    def insert(self, k):
        self.heap_list.append(k)
        self.heap_size = self.heap_size+1
        self.prec_up(self.heap_size)