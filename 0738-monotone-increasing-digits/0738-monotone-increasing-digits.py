class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        stk = list(s)
        print(stk)
        
        for i in range(len(stk) - 1):
            if stk[i] > stk[i + 1]:
                stk[i + 1:] = ['9'] * (len(stk) - (i + 1))
                stk[i] = str(int(stk[i]) - 1)
                while i > 0 and stk[i] < stk[i - 1]:
                    stk[i] = '9'
                    stk[i - 1] = str(int(stk[i - 1]) - 1)
                    i -= 1
                return int(''.join(stk))
        
        return int(''.join(stk))
