from collections import deque
from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        que = deque()
        
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    que.append((i, j))
                    isWater[i][j] = 0  # Water cells are height 0
                else:
                    isWater[i][j] = -1  # Land cells are unvisited
        
        while que:
            i, j = que.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r, c = i + dx, j + dy
                if 0 <= r < m and 0 <= c < n and isWater[r][c] == -1:
                    isWater[r][c] = isWater[i][j] + 1
                    que.append((r, c))
        
        return isWater
