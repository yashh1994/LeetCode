class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        stk_val = 0
        stk_wrd = ""
        
        for c in s:
            if c.isdigit():
                stk_val = stk_val * 10 + int(c)
            elif c == '[':
                stk.append((stk_wrd, stk_val))
                stk_wrd = ""
                stk_val = 0
            elif c == ']':
                prev_str, num = stk.pop()
                stk_wrd = prev_str + stk_wrd * num
            else:
                stk_wrd += c
        
        return stk_wrd