class Solution:
    def simplifyPath(self, path: str) -> str:
        path.replace("//","/")
        li = path.split("/")
        li = list(filter(lambda x:x != "" and x != ".",li))
        print(li)
        stk = []
        ans = ""
        for i in li:
            if i == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(i)
        for i in stk:
            ans += "/"
            ans += i
        return ans if ans else "/"

        