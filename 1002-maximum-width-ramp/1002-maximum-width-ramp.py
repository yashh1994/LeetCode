class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = [0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[stk[-1]] >= nums[i]:
                stk.append(i)
        for i in range(len(nums)-1,-1,-1):
            while stk and nums[stk[-1]] <= nums[i]:
                ans = max(ans,i-stk.pop())
        return ans
        