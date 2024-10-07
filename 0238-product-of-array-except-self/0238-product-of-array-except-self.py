class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multi_nm = 0
        ct_zero = 0
        for n in nums:
            if n == 0:
                ct_zero += 1
            if n != 0 and multi_nm == 0:
                multi_nm = n
            elif n != 0:
                multi_nm *= n 
        ans = [0]*len(nums)
        print(multi_nm)
        if ct_zero >= 2:
            return ans
        for i in range(len(nums)):
            n = nums[i]
            if n != 0 and ct_zero == 0:
                ans[i] = (multi_nm//n)
            elif n != 0:
                ans[i] = 0
            else:
                ans[i] = multi_nm
        return ans
        