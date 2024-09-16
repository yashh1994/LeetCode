class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        
        max_val = max(nums)
        cur = 0
        mx = 0
        st, ed = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == max_val:
                cur += 1
                mx = max(mx, cur)
            else:
                cur = 0  
        
        return mx
