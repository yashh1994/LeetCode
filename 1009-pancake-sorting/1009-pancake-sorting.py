class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        sor_li = sorted(arr)
        i = len(arr)-1
        while i >= 0:
            print(len(arr))
            if sor_li[i] == arr[i]:
                i-=1
                continue
            mx_in = arr.index(sor_li[i])
            arr = arr[:mx_in+1][::-1] + arr[mx_in+1:]
            arr = arr[:i+1][::-1] + arr[i+1:]
            ans.append(mx_in+1)
            ans.append(i+1)
            i-=1
        print(arr)
        return ans
        