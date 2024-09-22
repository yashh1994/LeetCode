class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i in s:
            if stk and stk[-1] == i:
                stk.pop()
            else:
                stk.append(i)
        return ''.join(stk)

        