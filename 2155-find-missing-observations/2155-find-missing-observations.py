class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_n = len(rolls) + n
        total_sum = total_n*mean
        rem_sum = total_sum-sum(rolls)
        if rem_sum/(n)>6.0 or rem_sum <= 0:
            return []
        ans = []
        eq = rem_sum//n
        if eq == 0:
            return []
        print(f"total sum: {total_sum} ")
        print(f"res sum: {rem_sum} ")
        for i in range(n-1):
            ans.append(eq)
        print(ans)
        print(rem_sum-(eq*(n-1)))
        if rem_sum-(eq*(n-1)) > 6:
            dis = rem_sum-(eq*(n-1)) - 6
            index = 0
            while dis > 0:
                t = 6-ans[index]
                if t <= dis:
                    ans[index] = ans[index] + t
                    print(f"index: {index}, {ans[index]}")
                else:
                    ans[index] = ans[index]+dis
                    break
                dis -= t
                index += 1
            ans.append(6)
        else:
            ans.append(rem_sum-(eq*(n-1)))
        print(ans)
        return ans

        