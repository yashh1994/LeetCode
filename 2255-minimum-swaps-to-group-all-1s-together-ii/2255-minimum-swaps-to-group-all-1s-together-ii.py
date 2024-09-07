class Solution:
    def minSwaps(self,nums):
        n = len(nums)
        win_s = sum(nums)
        sli_win = nums[:win_s]
        slide1s = sum(sli_win)
        max_wsiz = slide1s
        for i in range(n):
            if nums[(win_s + i) % n] == 1:
                slide1s += 1  
            if nums[i] == 1:
                slide1s -= 1  

            max_wsiz = max(max_wsiz, slide1s)
        return win_s - max_wsiz  