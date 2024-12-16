import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            ind = 0
            mn = nums[0]
            for i in range(len(nums)):
                if mn > nums[i]:
                    ind = i
                    mn = nums[i]
            nums[ind] *= multiplier
        return nums
        