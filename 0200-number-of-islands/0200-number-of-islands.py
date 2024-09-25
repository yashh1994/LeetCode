from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, visited):
            if visited[i][j]:
                return
            visited[i][j] = True
            
            if i - 1 >= 0 and grid[i - 1][j] == "1" and not visited[i - 1][j]:
                dfs(grid, i - 1, j, visited)
            if j - 1 >= 0 and grid[i][j - 1] == "1" and not visited[i][j - 1]:
                dfs(grid, i, j - 1, visited)
            if i + 1 < len(grid) and grid[i + 1][j] == "1" and not visited[i + 1][j]:
                dfs(grid, i + 1, j, visited)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == "1" and not visited[i][j + 1]:
                dfs(grid, i, j + 1, visited)

        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(grid, i, j, visited)
                    ans += 1
                    
        return ans
