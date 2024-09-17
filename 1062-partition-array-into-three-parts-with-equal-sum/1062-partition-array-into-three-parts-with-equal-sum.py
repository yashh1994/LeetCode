class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr) % 3 != 0:
            return False
        eq = sum(arr) // 3
        sm = 0
        ct = 0
        for i in arr:
            sm += i
            if sm == eq:
                ct += 1
                sm = 0
            print(sm)
        return ct >= 3
