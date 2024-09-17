class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(n-1):
            h = max(nums[-1]-k,nums[i]+k)
            l = min(nums[0]+k,nums[i+1]-k)
            ans = min(ans,h-l)
        return ans

        