class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        cur_d = 0
        if len(nums) <= 2:
            return 0
        st = 0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1] != cur_d:
                st = i-1
                cur_d = nums[i]-nums[i-1]
            if (i-st+1)-2 > 0:
                ans += (i-st+1)-2
        return ans
