class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        st = set()
        ans = []
        for n in nums:
            if n in st:
                ans.append(n)
            else:
                st.add(n)
        return ans 