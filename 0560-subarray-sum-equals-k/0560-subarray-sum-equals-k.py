from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        cur_sum = 0
        pre_sum[0] = 1
        ans = 0
        for n in nums:
            cur_sum += n
            if (cur_sum - k) in pre_sum:
                ans += pre_sum[cur_sum - k]
            pre_sum[cur_sum] += 1
        return ans
        
        