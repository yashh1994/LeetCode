class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.size = k
        

    def insertFront(self, value: int) -> bool:
        if len(self.arr) == self.size:
            return False
        self.arr.insert(0,value)
        return True

        

    def insertLast(self, value: int) -> bool:
        if len(self.arr) == self.size:
            return False
        self.arr.append(value)
        return True

        

    def deleteFront(self) -> bool:
        if self.arr:
            self.arr.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.arr:
            self.arr.pop(-1)
            return True
        return False
        

    def getFront(self) -> int:
        if self.arr:
            return self.arr[0]
        return -1
        

    def getRear(self) -> int:
        if self.arr:
            return self.arr[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return not self.arr
        

    def isFull(self) -> bool:
        return len(self.arr) == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()