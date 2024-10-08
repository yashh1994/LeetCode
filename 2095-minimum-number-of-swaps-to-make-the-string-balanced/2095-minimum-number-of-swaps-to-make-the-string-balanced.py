class Solution:
    def minSwaps(self, s: str) -> int:
        new_s = ""
        stk = []
        for c in s:
            if c == '[':
                stk.append(c)
            else:
                if stk:
                    stk.pop()
                else:
                    stk.append(']')
        return len(stk)//2

        