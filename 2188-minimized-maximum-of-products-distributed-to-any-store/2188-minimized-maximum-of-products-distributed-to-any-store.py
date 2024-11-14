import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_fit(dis):
            str_n = 0
            for q in quantities:
                str_n += ceil(q/dis)
            return str_n <= n

        min_d,max_d = 1,max(quantities)
        while min_d < max_d:
            mid = (max_d+min_d)//2
            if can_fit(mid):
                max_d = mid
            else:
                min_d = mid+1
        return min_d
        
        