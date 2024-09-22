class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_valid(s: str, t: str) -> bool:
            it = iter(t)
            return all(char in it for char in s)
        ans = -1
        for i in range(len(strs)):
            ch = True
            for j in range(len(strs)):
                if i != j and is_valid(strs[i],strs[j]):
                    ch = False
                    break
            if ch:
                ans = max(ans,len(strs[i]))
        return ans
