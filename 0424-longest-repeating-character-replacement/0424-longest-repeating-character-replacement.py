class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        ans = 0
        mp = {}
        
        while r < len(s):
            mp[s[r]] = mp.get(s[r], 0) + 1
            
            while (r - l + 1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                if mp[s[l]] <= 0:
                    del mp[s[l]]
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
            
        return ans
