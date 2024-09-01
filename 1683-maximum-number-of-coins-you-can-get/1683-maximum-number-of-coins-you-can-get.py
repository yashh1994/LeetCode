class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        pi = sorted(piles,reverse=True)
        index = 1
        ans = 0
        for i in range(len(piles)//3):
            ans += pi[index]
            index += 2
        return ans

        
        