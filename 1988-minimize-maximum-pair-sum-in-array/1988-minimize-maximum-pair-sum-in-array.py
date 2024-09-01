class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        l,r = 0,n-1
        while l<r:
            ans = max(ans,nums[l]+nums[r])
            l+=1
            r-=1
        return ans
        