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

    def prec_down(self, i):
        left_child  = i*2 +1 
        right_child = i*2 +2
        smallest_element = i 
        while i < self.heap_size :
            if left_child < self.heap_list[i]:
                smallest_element = left_child
            if right_child < smallest_element:
                smallest_element = right_child
            if i != smallest_element:
                self.heap_list[i], self.heap_list[smallest_element] = self.heap_list[smallest_element], self.heap_list[i]
            i = smallest_element

    def del_min(self):
        ret_val = self.heap_list[0]
        #swap 
        self.heap_list[0] = self.heap_list[self.heap_size]
        self.heap_size = self.heap_size - 1
        self.heap_list.pop()
        self.prec_down(1)
        return ret_val
    
    def build_heap(self, lst):
        self.heap_list = lst[:]
        self.heap_size = len(lst)
        i = len(lst)//2
        while i > 0 :
            self.prec_down(i)
            i = i - 1


