class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mn = 0
        mx = 0
        ans = 0
        mx_v = 0
        mn_v = 0
        for i,n in enumerate(arr):
            if n > mx_v:
                mx_v = n
                mx = n
            if mx <= i:
                ans += 1
                mn = i +1
        return ans
        