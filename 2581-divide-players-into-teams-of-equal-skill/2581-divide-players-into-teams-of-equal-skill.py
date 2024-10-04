class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        skill.sort()
        l,r = 0,len(skill)-1
        s = skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r] != s:
                return -1
            else:
                ans += (skill[l]*skill[r])
            l += 1
            r -= 1
        return ans
            

        