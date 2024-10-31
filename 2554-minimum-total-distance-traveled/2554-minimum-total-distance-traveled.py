from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n, m = len(robot), len(factory)
        
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = 0
        
        for i in range(m):
            position, capacity = factory[i]
            for j in range(n + 1):
                dp[i + 1][j] = dp[i][j]
            for j in range(n):
                total_distance = 0
                for k in range(min(capacity, n - j)):
                    total_distance += abs(position - robot[j + k])
                    dp[i + 1][j + k + 1] = min(dp[i + 1][j + k + 1], dp[i][j] + total_distance)

        return dp[m][n]
