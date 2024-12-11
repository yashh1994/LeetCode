from collections import Counter

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)
        l,r = 0,0
        ctn,maxCtn = 0,0
        fre = Counter(nums)
        while r <= mx:
            ctn += fre[r]
            while r-l > 2*k:
                ctn -= fre[l]
                l += 1
            maxCtn = max(maxCtn,ctn)
            r += 1
        return maxCtn
            

        