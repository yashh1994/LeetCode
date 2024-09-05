class Solution:
    def minFlips(self, target: str) -> int:
        # def swap(s,i) -> str:
        #     ans = s[:i]
        #     for k in range(i,len(s)):
        #         ans += '1' if s[k] == '0' else '0'
        #     return ans
        # ans = "0"*len(target)
        # ope = 0
        # for i in range(len(ans)):
        #     c = ans[i]
        #     if ans == target:
        #         return ope
        #     if c != target[i]:
        #         ans = swap(ans,i)
        #         ope += 1
        # return ope
        ans = 0
        ct = 0

        for c in target:
            cm = '1' if ct % 2 != 0 else '0'
            if c != cm:
                ct += 1
        return ct

             
        