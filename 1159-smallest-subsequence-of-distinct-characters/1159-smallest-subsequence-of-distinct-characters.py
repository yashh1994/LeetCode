class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if s[i] in stk:
                continue
            if not stk:
                stk.append(s[i])
            else:
                while stk and stk[-1] in s[i+1:] and stk[-1] > s[i]:
                    stk.pop()
                stk.append(s[i])
            print(stk)
        return ''.join(stk)
        