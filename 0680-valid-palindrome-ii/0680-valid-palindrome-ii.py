class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.is_pali(s[l:r]) or self.is_pali(s[l+1:r+1])
            l+=1
            r-=1
        return True
    
    def is_pali(self,s:str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
        