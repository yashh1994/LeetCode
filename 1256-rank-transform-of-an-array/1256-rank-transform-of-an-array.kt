class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        // Create a mutable set and add all elements from arr
        val nums = mutableSetOf<Int>()
        for (i in arr) {
            nums.add(i)
        }
        
        // Convert the set to a sorted list
        val sortedNums = nums.sorted()
        
        // Create a map to store the rank of each element
        val rankMap = mutableMapOf<Int, Int>()
        for ((index, value) in sortedNums.withIndex()) {
            rankMap[value] = index + 1
        }
        
        // Create the answer array by replacing each element with its rank
        val ans = IntArray(arr.size)
        for (i in arr.indices) {
            ans[i] = rankMap[arr[i]]!!
        }
        
        return ans
    }
}
