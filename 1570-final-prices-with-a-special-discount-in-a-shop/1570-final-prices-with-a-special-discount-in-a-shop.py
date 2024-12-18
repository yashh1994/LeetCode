class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(prices)
        ans[-1] = prices[-1]
        stk = [ans[-1]]
        for i in range(len(prices)-2,-1,-1):
            while stk and stk[-1] > prices[i]:
                stk.pop()
            if not stk:
                ans[i] = prices[i]
            else:
                ans[i] = prices[i] - stk[-1]
            stk.append(prices[i])
        return ans

        