class SummaryRanges:

    def __init__(self):
        self.arr = []
        self.st = set()
        

    def addNum(self, value: int) -> None:
        check = False
        if value in self.st:
            return
        
        for i, pair in enumerate(self.arr):
            if pair[1] + 1 == value:
                self.arr[i][1] = value
                check = True
                j = i + 1
                while j < len(self.arr) and self.arr[j][0] == self.arr[i][1] + 1:
                    self.arr[i][1] = self.arr[j][1]
                    del self.arr[j]  
            elif pair[0] - 1 == value:
                self.arr[i][0] = value
                check = True
                break

        if not check:
            self.arr.append([value, value])
            self.arr.sort()  
        self.st.add(value)

        
        
        

    def getIntervals(self) -> List[List[int]]:
        return self.arr
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()