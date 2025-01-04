# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def go(node):
            nonlocal ans
            nonlocal count 
            if not node or count > k or ans:
                return 
            
            go(node.left)
            count += 1
            if count == k:
                print("Node is :",node.val)
                ans = node
                return
            go(node.right)
        ans = None
        count = 0
        go(root)
        return ans.val if ans else -1

        