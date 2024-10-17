class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        cur = 1
        index = 2
        while len(s)<n:
            s += "1"*int(s[index]) if cur%2 == 1 else "2"*int(s[index])
            index += 1
            cur += 1
        print(s)
        return s[:n].count('1')

        