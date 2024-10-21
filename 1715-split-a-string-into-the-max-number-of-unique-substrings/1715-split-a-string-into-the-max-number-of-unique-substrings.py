class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def go(start, seen):
            if start == len(s):
                return len(seen)
            
            max_splits = 0
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, go(end, seen))
                    seen.remove(substring)
                    
            return max_splits
        
        return go(0, set())
