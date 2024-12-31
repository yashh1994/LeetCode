# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def go(node):
            if not self.ans:
                return
            if not node:
                return 0
            
            left = go(node.left)
            right = go(node.right)
            if not self.ans:
                return 
            if abs(left-right) > 1:
                self.ans = False
            return max(left,right)+1

        self.ans = True
        if not root:
            return True
        go(root) 
        return self.ans
        