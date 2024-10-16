from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        ans = ""
        if a > 0: heappush(q, [-a, 'a'])
        if b > 0: heappush(q, [-b, 'b'])
        if c > 0: heappush(q, [-c, 'c'])
        
        while q:
            fre, elem = heappop(q)
            fre = -fre
            if len(ans) >= 2 and ans[-1] == elem and ans[-2] == elem:
                if q:
                    sec_fre, sec_elem = heappop(q)
                    sec_fre = -sec_fre
                    ans += sec_elem
                    sec_fre -= 1
                    if sec_fre > 0:
                        heappush(q, [-sec_fre, sec_elem])
                else:
                    return ans
                heappush(q, [-fre, elem])
            else:
                ans += elem
                fre -= 1
                if fre > 0:
                    heappush(q, [-fre, elem])
        
        return ans
