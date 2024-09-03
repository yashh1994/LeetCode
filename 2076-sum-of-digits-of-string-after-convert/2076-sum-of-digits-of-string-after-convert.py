class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sum_it(s):
            ans = 0
            for c in s:
                ans += int(c)
            return ans

        
        ans = ""
        for c in s:
            ans += str(ord(c)-96)
        for i in range(k):
            ans = str(sum_it(ans))        
        return int(ans)
