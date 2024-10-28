from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_st = set(nums)
        ans = 1

        for n in nums:
            if n in num_st:
                index = 1
                nm = n
                while nm * nm in num_st:
                    nm *= nm
                    index += 1
                ans = max(ans, index)

        return ans if ans > 1 else -1
