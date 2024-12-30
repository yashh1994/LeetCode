from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque([(root, 0)])  
        max_width = 0
        
        while que:
            level_size = len(que)
            _, first_index = que[0] 
            _, last_index = que[-1] 
            
            max_width = max(max_width, last_index - first_index + 1)
            
            for _ in range(level_size):
                node, index = que.popleft()
                if node.left:
                    que.append((node.left, 2 * index))
                if node.right:
                    que.append((node.right, 2 * index + 1))
        
        return max_width
