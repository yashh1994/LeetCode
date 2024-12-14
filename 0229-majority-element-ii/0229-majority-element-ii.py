class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nm1,nm2 = -float('inf'),-float('inf')
        ctn1,ctn2 = 0,0
        for n in nums:
            if ctn1 == 0 and nm2 != n:
                ctn1 = 1
                nm1 = n
            elif ctn2 == 0 and nm1 != n:
                ctn2 = 1
                nm2 = n
            elif nm1 == n:
                ctn1 += 1
            elif nm2 == n:
                ctn2 += 1
            else:
                ctn1 -= 1
                ctn2 -= 1
        ans = []
        if nums.count(nm1) > len(nums)//3:
            ans.append(nm1)
        if nums.count(nm2) > len(nums)//3:
            ans.append(nm2)
        return ans
