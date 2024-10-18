class Solution {
    var maxOr = 0
    var ans = 0

    fun countMaxOrSubsets(nums: IntArray): Int {
        for (num in nums) {
            maxOr = maxOr or num
        }
        go(nums, 0, 0)
        
        return ans
    }

    fun go(nums: IntArray, index: Int, cur: Int) {
        if (index == nums.size) {
            if (cur == maxOr) {
                ans++
            }
            return
        }
        go(nums, index + 1, cur or nums[index])
        go(nums, index + 1, cur)
    }
}
