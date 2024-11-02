class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        li = []
        for n in nums:
            if not li or li[-1] != n:
                li.append(n)
        index = 0
        while index<len(li):
            nums[index] = li[index]
            index += 1
        return index
        