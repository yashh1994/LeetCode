from heapq import heappop,heappush
import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        for i in nums:
            heappush(heap,-i)
        for i in range(k):
            poped_e = -heappop(heap)
            nm = ceil(poped_e/3)
            ans += poped_e
            heappush(heap,-nm)
        return ans
        
        