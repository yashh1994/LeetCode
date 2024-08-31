class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans=0
        pre_stk = []
        path_stk = []
        chk = False
        word = ""
        input = input.replace("\\n", "*n")
        input = input.replace("\\t", "*t")

        input = input.replace("\\n", "\n").replace("\\t", "\t")
        print(input.splitlines())

        stk = []
        for line in input.splitlines():
            cou = line.count('\t')
            for i in range(len(stk)-cou):
                stk.pop()
            stk.append(line)
            if '.' in line:
                sm = 0
                for s in stk:
                    sm += len(s)
                ans = max(ans, sm - 1 + len(stk) - (cou * (cou + 1)) // 2)

            print(stk)
        return ans