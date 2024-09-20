class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        new_s = s + "#" + rev_s

        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = compute_lps(new_s)
        to_add = rev_s[:len(s) - lps[-1]]
        
        return to_add + s
