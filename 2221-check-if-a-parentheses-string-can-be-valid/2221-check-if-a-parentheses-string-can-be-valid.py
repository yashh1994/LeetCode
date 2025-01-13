class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        opt = []
        str_opt = []
        for i,c in enumerate(s):
            if locked[i] == '0':
                opt.append(i)
            else:
                if c == ')':
                    if len(str_opt) > 0:
                        str_opt.pop()
                    elif opt:
                        opt.pop()
                    else:
                        return False
                else:
                    str_opt.append(i)
        print(f"opt: {opt} str_opt: {str_opt}")
        while opt and str_opt and opt[-1] > str_opt[-1]:
            str_opt.pop()
            opt.pop()
        if not str_opt and opt:
            return len(opt)%2 == 0
        print(f"opt: {opt} str_opt: {str_opt}")
        return not opt and not str_opt
                    