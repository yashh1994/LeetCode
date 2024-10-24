class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        
        return go(root1, root2);
    }

    private boolean go(TreeNode node1, TreeNode node2) {
        if (node1 == null && node2 == null) {
            return true;
        }
        if (node1 == null || node2 == null || node1.val != node2.val) {
            return false;
        }

        return (go(node1.left, node2.left) || go(node1.left, node2.right)) &&
               (go(node1.right, node2.right) || go(node1.right, node2.left));
    }
}