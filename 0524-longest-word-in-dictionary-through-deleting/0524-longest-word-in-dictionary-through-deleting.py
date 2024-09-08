from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def com_str(s1: str, s2: str) -> bool:
            i1, i2 = 0, 0
            while i1 < len(s1) and i2 < len(s2):
                if s1[i1] == s2[i2]:
                    i2 += 1
                i1 += 1
            return i2 == len(s2)
        
        valid_words = [word for word in dictionary if len(word) <= len(s) and com_str(s, word)]
        
       
        return min(valid_words, key=lambda word: (-len(word), word), default="")
