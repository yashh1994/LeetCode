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

        # print(input)
        # for i, c in enumerate(input):
        #     print(c)
        #     if ord(c) == 92:  
        #         print("Yeash")
        #         chk = True
        #         continue
        #     elif (c == 'n' or c == 't') and chk:
        #         chk = False
        #         if c == 'n':  # Newline handling
        #             path_stk.append(word)
        #             word = ""
        #             pre_stk = path_stk[:]
        #             path_stk.clear()
        #         else:  # Tab handling
        #             path_stk.append(pre_stk.pop(0))
        #     elif c == '.':  # Handling for file extensions
        #         t = i
        #         while t < len(input) and input[t] != '\\':
        #             word += input[t]
        #             t += 1
        #         path_stk.append(word)
        #         word = ""
        #         ans.append(path_stk[:])  # Capture the current path
        #     else:
        #         word += c

        # print(ans)
        return 0

