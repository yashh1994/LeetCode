class Solution:
    def maximumSwap(self, num: int) -> int:
        li = list(map(int,str(num)))
        sort_li = sorted(li,reverse=True)
        i = 0
        while i < len(li) and sort_li[i]==li[i]:
            i += 1
        if i == len(li):
            return num
        t = len(li)-1
        while t >= i and li[t] != sort_li[i]:
            t -= 1
        li[t] = li[i]
        li[i]=sort_li[i]
        ans = 0
        for n in li:
            ans *= 10
            ans += n
        return ans
        