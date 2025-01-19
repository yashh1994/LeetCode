import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        n, m = len(heightMap), len(heightMap[0])
        
        # Min-heap to store the boundary cells
        min_heap = []
        visited = [[False] * m for _ in range(n)]
        
        # Add all boundary cells to the heap and mark them as visited
        for i in range(n):
            for j in [0, m-1]:  # First and last column
                heapq.heappush(min_heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        
        for j in range(m):
            for i in [0, n-1]:  # First and last row
                if not visited[i][j]:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Directions for the four possible neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        trapped_water = 0
        
        # Process the heap
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            
            # Check the four neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Calculate the trapped water
                    if height > heightMap[nx][ny]:
                        trapped_water += height - heightMap[nx][ny]
                    # Push the neighbor into the heap with the updated height
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return trapped_water
