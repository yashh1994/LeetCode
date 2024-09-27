class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        li = [0]*(n+1)
        if n <= 1:
            return n
        li[0] = 0
        li[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                li[i] = li[i//2]
            else:
                li[i] = li[(i//2)]+li[(i//2)+1]
        print(li)
        return max(li)





        