class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mx = mn = nums[0]
        for n in nums[1:]:
            mx,mn = max(mx, mx*n, n, mn*n),min(mn, mn*n, n, mx*n)
        return mx
        