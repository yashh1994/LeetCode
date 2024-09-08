from collections import Counter

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def com_str(s1:str,s2:str) -> bool:
            i1,i2 = 0,0
            print(f'Checking {s1} {s2}')
            while i1<len(s1) and i2<len(s2):
                if s1[i1] == s2[i2]:
                    i1 += 1
                    i2 += 1
                else:
                    i1 += 1
            print(i1,' ',i2)
            if i2 < len(s2):
                return False
            return True

        ans = ""
        for st in dictionary:
            if com_str(s,st):
                if not ans or len(ans) < len(st):
                    ans = st
                elif len(ans) == len(st) and st < ans:
                    ans = st
                 
        return ans
        
        