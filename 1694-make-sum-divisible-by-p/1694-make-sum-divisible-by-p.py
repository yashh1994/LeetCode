class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mp = {0:-1}
        cur_m = 0
        ans = len(nums)
        total_m = sum(nums)%p
        if total_m == 0:
            return 0
        for i,nm in enumerate(nums):
            cur_m = (cur_m+nm)%p
            tar_m = (cur_m - total_m)%p
            if tar_m in mp:
                ans = min(ans,i-mp[tar_m])
            mp[cur_m] = i
        return ans if ans<len(nums) else -1
        