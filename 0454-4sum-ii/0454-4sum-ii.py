class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        st = set()
        n = len(nums1)
        mp = {}
        for i in range(n):
            for j in range(n):
                s = (nums1[i]+nums2[j])*(-1)
                if s in st:
                    mp[s] += 1
                else:
                    mp[s] = 1
                    st.add(s)
        print(mp,' ',st)
        ans = 0
        for i in range(n):
            for j in range(n):
                sm = nums3[i]+nums4[j]
                if sm in st:
                    ans += (mp[sm])
        return ans
        