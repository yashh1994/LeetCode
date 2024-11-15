# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def go(node,val):
            if not node:
                return
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    go(node.right,val)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    go(node.left,val) 
        if not root:
            return TreeNode(val)
        go(root,val)
        return root

        