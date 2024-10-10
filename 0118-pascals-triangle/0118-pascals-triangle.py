class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cur_l = [1]
        ans = [cur_l]
        for i in range(1,numRows):
            new_c = [1]
            for i in range(1,len(cur_l)):
                new_c.append(cur_l[i]+cur_l[i-1])
            new_c.append(1)
            ans.append(new_c)
            cur_l = new_c
        return ans
        