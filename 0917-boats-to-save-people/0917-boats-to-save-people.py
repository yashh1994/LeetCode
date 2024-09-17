class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        l,r = 0,len(people)-1
        while l <= r:
            if people[l]+people[r] <= limit:
                l += 1
            r -= 1
            ans += 1
        return ans
        