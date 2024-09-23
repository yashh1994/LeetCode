from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        n = len(points)
        ans = 0
        
        for i in range(n):
            dis = defaultdict(int)
            for j in range(n):
                if i != j:
                    d = distance(points[i], points[j])
                    dis[d] += 1
            
            
            for k, v in dis.items():
                if v >= 2:
                    ans += v * (v - 1)  
        
        return ans
