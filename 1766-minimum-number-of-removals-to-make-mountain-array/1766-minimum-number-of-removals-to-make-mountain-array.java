class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;
        
        int[] leftS = new int[n];
        for (int i = 0; i < n; i++) {
            leftS[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    leftS[i] = Math.max(leftS[i], leftS[j] + 1);
                }
            }
        }
        int[] rightS = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            rightS[i] = 1;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[i]) {
                    rightS[i] = Math.max(rightS[i], rightS[j] + 1);
                }
            }
        }
        int ans = 0;
        for (int i = 1; i < n - 1; i++) {
            if (leftS[i] > 1 && rightS[i] > 1) {
                ans = Math.max(ans, leftS[i] + rightS[i] - 1);
            }
        }
        return n - ans;
    }
}
