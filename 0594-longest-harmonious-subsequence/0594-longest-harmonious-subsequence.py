from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp = Counter(nums)
        ans = 0
        for key in mp.keys():
            if key+1 in mp:
                ans = max(ans,mp[key]+mp[key+1])
        return ans
