# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def go(node1,node2):
            if node1 or node2:
                sm = (node1.val if node1 else 0)+(node2.val if node2 else 0)
                node = TreeNode(sm)
                node.left = go(node1.left if node1 else None,node2.left if node2 else None)
                node.right = go(node1.right if node1 else None,node2.right if node2 else None)
                return node
        return go(root1, root2)
        
            


        