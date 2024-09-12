class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for w in words:
            print(''.join(set(w)))
            if all([True if c in allowed else False for c in ''.join(set(w))]):
                ans += 1
        return ans
        