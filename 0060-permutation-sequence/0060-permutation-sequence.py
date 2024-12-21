from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def get_n(seq, k):
            if not seq:
                return ""
            each = factorial(len(seq) - 1)
            nth = (k - 1) // each
            return seq[nth] + get_n(seq[:nth] + seq[nth + 1:], (k - 1) % each + 1)
        
        seq = ''.join(str(i + 1) for i in range(n))
        return get_n(seq, k)
