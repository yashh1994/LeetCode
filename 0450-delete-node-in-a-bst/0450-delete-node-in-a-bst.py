# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def del_node(node):
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            most_right_node = most_right(node.left)
            most_right_node.right = node.right
            return node.left

        def most_right(node):
            if not node.right:
                return node
            return most_right(node.right)

        if root is None:
            return root
        
        if root.val == key:
            return del_node(root)
        
        ans = root
        
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = del_node(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = del_node(root.right)
                    break
                else:
                    root = root.right
                    
        return ans
