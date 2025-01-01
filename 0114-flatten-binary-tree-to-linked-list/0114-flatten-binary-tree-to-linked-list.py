# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        temp = root
        while temp:
            if temp.left:
                t1 = temp.left
                while t1.right:
                    t1 = t1.right
                t1.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
            
        