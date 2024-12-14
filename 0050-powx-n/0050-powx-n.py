class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        rem_pow = abs(n)
        while rem_pow:
            if rem_pow % 2:
                ans *= x
                rem_pow -= 1
            else:
                x *= x
                rem_pow /= 2
        if n < 0:
            return 1.0/ans
        return ans
        