from collections import Counter 
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            counter = Counter(nums)
            return sum([1 if ct >= 2 else 0 for (k,ct) in counter.items()])
        st_nm = set(nums)
        ans = 0
        for nm in st_nm:
            if nm + k in st_nm:
                ans += 1
            if nm-k in st_nm:
                ans += 1
        return ans // 2
        

        