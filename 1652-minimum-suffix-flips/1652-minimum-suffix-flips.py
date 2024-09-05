class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        ct = 0

        for c in target:
            cm = '1' if ct % 2 != 0 else '0'
            if c != cm:
                ct += 1
        return ct

             
        