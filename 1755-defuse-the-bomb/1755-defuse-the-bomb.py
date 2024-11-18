class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            index = k
            cur_sum = sum(code[1:k+1])
            ans = [cur_sum]
            for i in range(1,n):
                cur_sum -= code[i]
                index = (index+1)%n
                cur_sum += code[index]
                ans.append(cur_sum)
            return ans
        else:
            index = n+k-1
            cur_sum = sum(code[index:index+(k*-1)])
            ans = [cur_sum]
            for i in range(n-2,-1,-1):
                cur_sum -= code[i]
                index = index-1 if index-1 >= 0 else n-1
                cur_sum += code[index]
                ans.append(cur_sum)
            return ans[::-1]





        