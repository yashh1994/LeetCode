class NestedIterator:
    def get_list(self, a):
        temp = []
        if a.isInteger():
            temp.append(a.getInteger())
        else:
            for ni in a.getList():
                temp.extend(self.get_list(ni))
        return temp

    def __init__(self, nestedList: [NestedInteger]):
        self.li = []
        for a in nestedList:
            self.li.extend(self.get_list(a))  # Flatten the nested list into self.li

    def next(self) -> int:
        return self.li.pop(0)

    def hasNext(self) -> bool:
        return len(self.li) > 0

# Example usage:
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
