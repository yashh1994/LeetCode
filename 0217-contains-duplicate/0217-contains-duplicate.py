class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for i in nums:
            st.add(i)
        return len(st) != len(nums)