from collections import Counter

class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        count = 1
        pre = word[0]
        for i in range(1,len(word)):
            c = word[i]
            if c == pre:
                count += 1
            else:
                ans += f"{count}{pre}"
                pre = c
                count = 1
            if count > 9:
                count -= 9
                ans += f"9{c}"
        ans += f"{count}{pre}"
        return ans
            
            
            


        