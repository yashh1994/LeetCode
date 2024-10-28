class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.ptr_st = 0
        self.size = k
        self.ptr_ed = 0
        self.is_full = False

    def enQueue(self, value: int) -> bool:
        if self.is_full:
            return False
        self.arr[self.ptr_st] = value
        self.ptr_st = (self.ptr_st + 1) % self.size
        if self.ptr_st == self.ptr_ed:
            self.is_full = True
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.is_full = False
        self.ptr_ed = (self.ptr_ed + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.ptr_ed]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.ptr_st - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return not self.is_full and self.ptr_st == self.ptr_ed

    def isFull(self) -> bool:
        return self.is_full
     


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()