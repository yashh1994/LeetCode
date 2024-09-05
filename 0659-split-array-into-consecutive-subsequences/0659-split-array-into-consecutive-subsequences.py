from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        need = defaultdict(int)

        for n in nums:
            freq[n] += 1

        for n in nums:
            if freq[n] == 0:
                continue

            if need[n] > 0:
                need[n] -= 1
                need[n + 1] += 1
            elif freq[n + 1] > 0 and freq[n + 2] > 0:
                freq[n + 1] -= 1
                freq[n + 2] -= 1
                need[n + 3] += 1
            else:
                return False

            freq[n] -= 1

        return True
