from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def cal_sp(li, mx):
            if len(li) == 1:
                return [mx - len(li[0])]  
            need = mx - sum(len(s) for s in li)
            sp = [need // (len(li) - 1) for _ in range(len(li) - 1)]
            ex = need % (len(li) - 1)
            for i in range(ex):
                sp[i] += 1
            return sp
        
        def join_sp_wr(li, sp):
            if len(li) == 1:  
                return li[0] + " " * sp[0]  
            ans = ""
            for i in range(len(sp)):
                ans += li[i]
                ans += " " * sp[i]
            ans += li[-1]  
            return ans    

        ans = []
        li = []
        for w in words:
            if not li or sum(len(s) for s in li) + len(li) + len(w) <= maxWidth:
                li.append(w)
            else:
                sp = cal_sp(li, maxWidth) 
                ans.append(join_sp_wr(li, sp))
                li = [w]  

        if li:
            last_line = " ".join(li) + " " * (maxWidth - len(" ".join(li)))
            ans.append(last_line)

        return ans
