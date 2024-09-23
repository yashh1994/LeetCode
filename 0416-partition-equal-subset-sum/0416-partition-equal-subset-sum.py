class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm%2!=0:
            return False
        eq = sm//2
        dp = [False]*(eq+1)
        dp[0] = True
        for n in nums:
            for i in range(eq,n-1,-1):
                dp[i] = dp[i] or dp[i-n]
        return dp[eq]
        