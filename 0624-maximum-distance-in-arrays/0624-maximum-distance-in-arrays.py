class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        dis = 0
        ar = sorted(arrays, key=lambda x: x[-1])
        for i in range(0,len(arrays)-1):
            n = ar[i]
            dis = max(dis,ar[-1][-1]-n[0])
            dis = max(dis,abs(n[-1]-ar[-1][0]))
        return dis
        