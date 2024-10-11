class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        if n <= 2:
            return 0
        arr = [True]*(n)
        nm = 2
        arr[0] = False
        arr[1] = False
        while nm*nm < n:
            if is_prime(nm):
                for i in range(nm*nm,n,nm):
                    arr[i] = False
            nm += 1
        return sum([1 if i else 0 for i in arr])





        