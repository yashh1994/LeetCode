from collections import defaultdict
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = Counter(s1)
        if len(s2) < len(s1):
            return False
        mp2 = defaultdict(int)
        
        for char in s2[:len(s1)]:
            mp2[char] += 1
        if mp == mp2:
            return True
        for i in range(len(s1), len(s2)):
            mp2[s2[i]] += 1
            mp2[s2[i - len(s1)]] -= 1
            if mp2[s2[i - len(s1)]] == 0:
                del mp2[s2[i - len(s1)]]

            if mp == mp2:
                return True

        return False
