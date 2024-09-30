class Solution:
    def isNumber(self, s: str) -> bool:
        def is_dig(s):
            if not s:
                return False
            nonlocal dig
            st = 0
            if "." in s:
                return False
            if s[0] == '-' or s[0] == '+':
                st += 1
            is_f = False 
            if not s[st:]:
                return False
            for i in range(st, len(s)):
                c = s[i]
                if c == '-' or c == '+':
                    return False
                if c not in dig and c != '.':
                    return False
                elif c == '.':
                    if is_f:
                        return False
                    is_f = True
            return True

        if not s:  
            return False

        dig = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        is_f = False  
        is_n = False
        st = 0
        
        if s[0] == '-' or s[0] == '+':
            st += 1
            
        if s[st:] == ".":
            return False
        if st == len(s):  
            return False

        
        for i in range(st, len(s)):
            if s[i] == '.':
                if is_f:
                    return False 
                is_f = True
            elif s[i] == 'e' or s[i] == 'E':
                if i + 1 < len(s) and is_n:
                    return is_dig(s[i + 1:])  
                else:
                    return False  
            elif s[i] not in dig:
                return False
            else:
                is_n = True
        
        return True