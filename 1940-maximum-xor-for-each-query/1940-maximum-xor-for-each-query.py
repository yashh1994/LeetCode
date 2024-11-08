from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor_val = (1 << maximumBit) - 1  
        ans = []
        cur_x = 0
        print(max_xor_val)
        for num in nums:
            cur_x ^= num

        for i in range(len(nums)):
            ans.append(cur_x ^ max_xor_val)
            cur_x ^= nums[-1 - i]

        return ans
