class Solution:
    def integerReplacement(self, n: int) -> int:
        def go(n: int, count: int):
            nonlocal ans  
            if n == 1:
                ans = min(ans, count)
                return
            if n <= 0 or ans < count:
                return
            if n % 2 == 0:
                go(n // 2, count + 1)
            else:
                go(n + 1, count + 1)
                go(n - 1, count + 1)

        ans = float('inf')  # Initialize ans to a large value
        go(n, 0)
        return ans
