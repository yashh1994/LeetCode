class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        score = 0
        sorted_in = sorted(range(n),key = lambda i: (nums[i],i))
        print(sorted_in)
        for i in sorted_in:
            if i not in st:
                score += nums[i]
                if i-1 >=0 :
                    st.add(i-1)
                if i+1 < n:
                    st.add(i+1)
        return score
    


        