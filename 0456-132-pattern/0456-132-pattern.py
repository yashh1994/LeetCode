class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stack = []
        second = -float('inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while stack and stack[-1] < nums[i]:
                second = stack.pop()
            stack.append(nums[i])

        return False
