class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0]*n
        per = primes[:]
        dp[0] = 1
        index = [0]*len(primes)
        for i in range(1,n):
            cur = min(per)
            dp[i] = cur
            
            for j in range(len(primes)):
                if per[j] == cur:
                    index[j] += 1
                    per[j] = primes[j]*dp[index[j]]
        return dp[-1]

        