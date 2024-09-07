class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        while k > 0:
            if nums[0] == 0:
                return sum(nums)
            elif nums[0] > 0:
                while k > 0:
                    nums[0] = nums[0]*(-1)
                    k-=1
                return sum(nums)
            elif nums[0] < 0:
                nums[0] = nums[0]*(-1)
                k-=1
                nums.sort()
        return sum(nums)

        