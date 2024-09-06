class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cur = 0
        ans = 0
        for c in s:
            if c == '(':
                cur += 1
            else:
                cur -= 1
                if cur == -1:
                    ans += 1
                    cur = 0
        return ans+cur

        