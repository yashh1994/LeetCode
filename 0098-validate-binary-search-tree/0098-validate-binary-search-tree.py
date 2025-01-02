# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def go(node, mn, mx):
            if not node:
                return True
            if not (mn < node.val < mx):
                return False 
            return go(node.left, mn, node.val) and go(node.right, node.val, mx)
        return go(root, float("-inf"), float("inf"))
        
        