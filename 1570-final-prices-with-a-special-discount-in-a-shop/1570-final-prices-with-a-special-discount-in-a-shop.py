class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):
            ch = False
            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i]-prices[j])
                    ch = True
                    break
            if not ch:
                ans.append(prices[i])
        return ans
        