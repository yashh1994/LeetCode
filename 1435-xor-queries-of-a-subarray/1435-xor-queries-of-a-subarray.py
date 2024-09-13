from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        a = [arr[0]]

        for i in range(1, len(arr)):
            a.append(a[-1] ^ arr[i])
        print(f"Left sided : {a}")

        for q in queries:
            in1 = q[0]
            in2 = q[1]

            if in1 > 0:
                ans.append(a[in2] ^ a[in1 - 1])
            else:
                ans.append(a[in2])

        return ans
