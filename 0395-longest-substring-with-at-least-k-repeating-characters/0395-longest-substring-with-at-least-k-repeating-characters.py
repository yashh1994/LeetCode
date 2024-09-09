class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        for a in set(s):
            
            if s.count(a) < k:
                return max(self.longestSubstring(t, k) for t in s.split(a))
        return len(s)