class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v = nums[0]
        for i in range(1,len(nums)):
            v = v ^ nums[i]
        return v
        