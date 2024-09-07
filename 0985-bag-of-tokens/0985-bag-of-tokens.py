class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        sc = 0
        l,r = 0,len(tokens)-1
        mx = 0
        while l<=r:
            do = False
            while l<=r and power >= tokens[l]:
                do = True
                power -= tokens[l]
                l += 1
                sc += 1
                mx = max(mx,sc)

            while l <= r and power < tokens[l] and sc > 0:
                do = True
                power += tokens[r]
                sc -= 1
                r -= 1
            if not do:
                break

        return mx
            
        