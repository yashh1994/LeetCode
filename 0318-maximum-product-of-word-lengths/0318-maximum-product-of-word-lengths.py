from collections import Counter

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mps = []
        for w in words:
            mps.append(set(Counter(w).keys()))
        print(mps)
        ans = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and all(True if c not in mps[i] else False for c in mps[j]):
                    ans = max(ans,len(words[i])*len(words[j]))

        return ans
        