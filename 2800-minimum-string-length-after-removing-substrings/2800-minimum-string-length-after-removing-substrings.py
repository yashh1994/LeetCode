class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if c == 'B' and stk and stk[-1] == 'A':
                stk.pop()
            elif c == 'D' and stk and stk[-1] == 'C':
                stk.pop()
            else:
                stk.append(c)
        return len(stk)
        