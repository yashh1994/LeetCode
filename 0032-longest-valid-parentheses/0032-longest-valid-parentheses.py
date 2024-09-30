class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        ans = 0
        stk.append(-1)
        for i,c in enumerate(s):
            if c == '(':
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    ans = max(ans,i - stk[-1])
        return ans
        