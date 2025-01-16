class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ans = 0
        count = sum([num2 >> i & 1 for i in range(32)]) 
        
        for i in range(31, -1, -1):
            if count == 0:
                break  
            ith = (num1 >> i) & 1
            if ith:
                count -= 1  
            ans |= ith << i
        if count:
            for i in range(32):
                if count == 0:
                    break
                ith = (ans >> i) & 1
                if ith == 0:
                    ans |= (1 << i)  # Set ith bit of ans to 1
                    count -= 1
        
        return ans
