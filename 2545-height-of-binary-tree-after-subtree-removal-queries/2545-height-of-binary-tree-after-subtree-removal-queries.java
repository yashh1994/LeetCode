import java.util.HashMap;
import java.util.Map;
class Solution {
    int[] ans;
    Map<Integer, Integer> map;
    Map<Integer, Integer> Height;
    int maxD = 0;
    public int[] treeQueries(TreeNode root, int[] queries) {
        int n = queries.length;
        ans = new int[n];
        map = new HashMap<>();
        Height = new HashMap<>();
        go(root,0,0);
        for (int i = 0; i < n; i++) {
            ans[i] = map.get(queries[i]);
        }
        return ans;
    }

    public int calH(TreeNode node){
        if(node == null){
            return -1;
        }
        if (Height.containsKey(node.val)){
            return Height.get(node.val);
        }
        int v = 1+Math.max(calH(node.left),calH(node.right));
        Height.put(node.val,v);
        return v;
    }

    public void go(TreeNode node, int curHeight,int max) {
        if (node == null) {
            return;
        }
        map.put(node.val,max);
        go(node.left,curHeight+1,Math.max(max,curHeight+1+calH(node.right)));
        go(node.right,curHeight+1,Math.max(max,curHeight+1+calH(node.left)));
        return;
        // int leftHeight = go(node.left, curHeight + 1);
        // int rightHeight = go(node.right, curHeight + 1);
        // int max = Math.max(leftHeight, rightHeight);
        // map.put(leftHeight, );
        // return max;
    }
}
