class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i,c in enumerate(s):
            if c in mp:
                mp[c][1] = i
            else:
                mp[c] = [i,i]
        print(mp)
        li = list(mp.values())
        ans = []
        ans.append(li[0])
        mainAns = [ans[-1][1]-ans[-1][0]+1]
        for i in range(1,len(li)):
            if ans[-1][1] >= li[i][0]:
                ans[-1][0] = min(li[i][0],ans[-1][0])
                ans[-1][1] = max(li[i][1],ans[-1][1])
                mainAns[-1] = ans[-1][1]-ans[-1][0]+1
            else:
                ans.append(li[i])
                mainAns.append(ans[-1][1]-ans[-1][0]+1)
        print(ans)
        return mainAns

        