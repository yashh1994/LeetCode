class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sm = sum(chalk)
        rm = k%sm
        for i,c in enumerate(chalk):
            rm -= c
            if rm < 0:
                return i
        return -1
        