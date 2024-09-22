from collections import Counter

class Solution:

    def __init__(self, nums: List[int]):
        self.mp = {}
        for i,n in enumerate(nums):
            if n not in self.mp:
                self.mp[n] = []
            self.mp[n].append(i)
        print(self.mp)
        self.ar = {a: 0 for a in nums}
        print(self.ar)

    def pick(self, target: int) -> int:
        vl = self.mp[target][self.ar[target]]
        self.ar[target] = (self.ar[target]+1)%len(self.mp[target])
        print(self.ar)
        return vl

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)