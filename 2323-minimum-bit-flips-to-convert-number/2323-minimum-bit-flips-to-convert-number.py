class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        str1 = bin(start)[2:]
        str2 = bin(goal)[2:]
        i,j = len(str1)-1,len(str2)-1
        if len(str1)>len(str2):
            str2 = "0"*(len(str1)-len(str2))+str2
        elif len(str1) < len(str2):
            str1 = "0"*(len(str2)-len(str1))+str1
        ct = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                ct += 1
            
        return ct
        