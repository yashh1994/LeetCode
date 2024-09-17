class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        mp = {}
        for w in list(s2.split(" ")):
            if w in mp:
                mp[w] += 1
            else:
                mp[w] = 1
        for w in list(s1.split(" ")):
            if w in mp:
                mp[w] += 1
            else:
                mp[w] = 1
        print(mp)
        for (k,v) in mp.items():
            if v == 1:
                ans.append(k)
        return ans
