class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        li = []
        last_time = neededTime[0]
        li.append(colors[0])
        for i in range(1,len(colors)):
            if colors[i] == li[-1]:
                if last_time < neededTime[i]:
                    ans += last_time
                    last_time = neededTime[i]
                else:
                    ans += neededTime[i]
            else:
                li.append(colors[i])
                last_time = neededTime[i]
        return ans

        