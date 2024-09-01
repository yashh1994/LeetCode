class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = 0
        n = len(nums)
        if n < 3:
            return 0
        for i in range(n-1,1,-1):
            a,b = 0,i-1
            while a<b:
                if nums[a]+nums[b] > nums[i]:
                    ans += (b-a)
                    b-=1
                else:
                    a+=1
        return ans


                
            
        return ans


        