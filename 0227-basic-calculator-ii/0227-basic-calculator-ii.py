import re

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        li = re.findall(r'\d+', s)
        li = [int(num) for num in li]  
        
        sym = []
        for c in s:
            if c in {'*', '/', '-', '+'}:
                sym.append(c)
        
        num = [li[0]]
        for i in range(len(sym)):
            if sym[i] == '*':
                num[-1] *= li[i + 1]  
            elif sym[i] == '/':
                num[-1] //= li[i + 1]  
            else:
                num.append(li[i + 1])  
        
        sym = [op for op in sym if op in {'+', '-'}]
        
        ans = num[0]
        for i in range(len(sym)):
            if sym[i] == '+':
                ans += num[i + 1]
            else:
                ans -= num[i + 1]
        
        return ans
