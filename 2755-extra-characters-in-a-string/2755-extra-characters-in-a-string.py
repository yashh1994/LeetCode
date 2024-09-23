class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        words = set(dictionary)
        
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if s[i:j] in words:
                    dp[j] = min(dp[j], dp[i])
                else:
                    dp[j] = min(dp[j], dp[i] + (j - i))
        
        return dp[n]