class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def de(s):
            return True if s == "t" else False
        
        stk = []
        for ch in expression:
            if ch in ["t", "f"]:
                stk.append(de(ch))
            elif ch == ")":
                expr = []
                while stk[-1] != "(":
                    expr.append(stk.pop())
                stk.pop()  
                op = stk.pop()
                if op == "&":
                    stk.append(all(expr))
                elif op == "|":
                    stk.append(any(expr))
                elif op == "!":
                    stk.append(not expr[0])
            elif ch in ["&", "|", "!", "("]:
                stk.append(ch)
                
        return stk[-1]
