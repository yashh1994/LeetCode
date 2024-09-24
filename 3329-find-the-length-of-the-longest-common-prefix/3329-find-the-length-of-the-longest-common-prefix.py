class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        st = set()
        for dig in arr1:
            s = str(dig)
            for i in range(1,len(s)+1):
                st.add(s[:i])
        print(st)
        ans = 0
        for dig in arr2:
            s = str(dig)
            for i in range(len(s),0,-1):
                if s[:i] in st:
                    ans = max(ans,i)
                    break
                if i < ans:
                    break
        return ans


        