class Solution:
    def check(self, nums: List[int]) -> bool:
        mn = min(nums)
        for i in range(len(nums)):
            if nums[i] == mn:
                check = True
                j = (i+1)%len(nums)
                while j != i:
                    if nums[j] < nums[j-1]:
                        check = False
                        break
                    j = (j+1)%len(nums)
                if check:
                    return True
        return False
        