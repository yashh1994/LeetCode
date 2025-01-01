# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def go(l,r):
            if (l is None) ^ (r is None):
                return False
            if not l and not r:
                return True
            if l.val != r.val:
                return False
            return go(l.left,r.right) and go(l.right,r.left)
        return go(root.left,root.right)

        