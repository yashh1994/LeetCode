/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1){
            TreeNode newHead = new TreeNode(val);
            newHead.left = root;
            return newHead;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        int counter = 1;
        while (counter < depth-1){
            int size = q.size();
            for(int i = 0; i < size; i++){
                TreeNode node = q.poll();
                if (node.left != null){
                    q.offer(node.left);
                }
                if(node.right != null){
                    q.offer(node.right);
                }
            }
            counter++;
        }
        int size = q.size();
        for(int i = 0; i < size; i++){
            TreeNode node = q.poll();
            
            TreeNode l = node.left;
            node.left = new TreeNode(val);
            node.left.left = l;

            TreeNode r = node.right;
            node.right = new TreeNode(val);
            node.right.right = r;
        }
        return root;
    }
}