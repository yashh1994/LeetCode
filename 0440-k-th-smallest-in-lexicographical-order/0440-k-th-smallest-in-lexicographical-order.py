class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def with_in(a,b,n):
            gap = 0
            while a <= n:
                gap += min(n+1,b) - a
                a *= 10
                b *= 10
            return gap
        i = 1
        num = 1
        while i < k:
            nm = with_in(num,num+1,n)
            if i+nm <= k:
                i += nm
                num += 1
            else:
                i += 1
                num *= 10
        return num
        