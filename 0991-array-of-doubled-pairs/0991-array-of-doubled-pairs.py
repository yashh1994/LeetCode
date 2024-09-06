class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        po = []
        neg = []
        ze = 0
        for n in arr:
            if n < 0:
                neg.append(n)
            elif n == 0:
                ze += 1
            else:
                po.append(n)
        ans = 0
        ans += (ze//2)
        po.sort()
        li = po[:]
        for i in po:
            if i in li and i*2 in li:
                ans += 1
                li.remove(i*2)
                li.remove(i)
        neg.sort(reverse = True)
        li = neg[:]
        for i in neg:
            if i in li and i*2 in li:
                ans += 1
                li.remove(i*2)
                li.remove(i)
        return ans == (len(arr)//2)
            
        