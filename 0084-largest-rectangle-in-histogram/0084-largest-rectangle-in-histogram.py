class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                hei = heights[stk.pop()]
                width = i if not stk else i-stk[-1]-1
                are = hei*width
                ans = max(ans,are)

            stk.append(i)
        
        n = len(heights)
        while stk:
            h = heights[stk.pop()]
            width = n if not stk else n - stk[-1] - 1
            ans = max(ans,h*width)
            

        return ans 
        