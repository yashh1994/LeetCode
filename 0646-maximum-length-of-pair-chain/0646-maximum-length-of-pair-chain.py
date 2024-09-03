class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key=lambda p:p[1])
        ans = 1
        cur = pairs[0]
        for i in range(1,len(pairs)):
            if pairs[i][0] > cur[1]:
                ans += 1
                cur = pairs[i]
        return ans
        