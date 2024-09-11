from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def go(cur: str, k: int, n: int):
            if len(cur) == n:
                self.ans.add(int(cur))
                return 
            if int(cur[-1]) + k < 10:
                go(cur + str(int(cur[-1]) + k), k, n)
            if int(cur[-1]) - k >= 0:
                go(cur + str(int(cur[-1]) - k), k, n)

        self.ans = set()
        for i in range(1, 10):  
            go(str(i), k, n)
        
        return list(self.ans)
