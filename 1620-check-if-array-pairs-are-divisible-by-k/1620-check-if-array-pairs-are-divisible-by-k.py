from collections import Counter
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rm_ct = Counter(n % k for n in arr)
        
        for rem in range(k):
            if rem == 0:
                if rm_ct[rem] % 2 != 0:
                    return False
            else:
                if rm_ct[rem] != rm_ct[k - rem]:
                    return False
        
        return True
