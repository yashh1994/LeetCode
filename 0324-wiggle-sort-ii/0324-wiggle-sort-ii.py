from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        mid = (len(nums) + 1) // 2
        left = nums[:mid][::-1]
        right = nums[mid:][::-1]

        for i in range(len(nums)):
            nums[i] = left.pop(0) if i % 2 == 0 else right.pop(0)
