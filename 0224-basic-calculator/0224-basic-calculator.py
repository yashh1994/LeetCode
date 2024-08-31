class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        word = ""
        stk = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                if word:
                    stk.append(word)
                    word = ""
            elif c == ')':
                a = eval(word)
                if stk:
                    word = stk.pop() + str(a)
                else:
                    word = str(a)
            else:
                word += c
            i += 1
        return eval(word)

                

                
                    


        