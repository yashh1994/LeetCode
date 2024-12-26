import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_h = []
        ans = []
        mp = defaultdict(int)
        for i in nums:
            mp[i] += 1
        for key,v in mp.items():
            heappush(min_h,(-v,key))
        while len(ans) < k:
            val,key = heappop(min_h)
            ans.append(key)
            print(f"Len: {len(ans)} {k}")
        return ans
        