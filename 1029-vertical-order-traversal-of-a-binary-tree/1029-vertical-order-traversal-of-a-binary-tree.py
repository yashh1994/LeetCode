from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        que = []
        ans = []
        if not root:
            return []
        que.append((root,(0,0)))

        while que:
            node,(row,col) = que.pop(0)
            mp[col].append((row, node.val))
            if node.left:
                que.append((node.left,(row+1,col-1)))
            if node.right:
                que.append((node.right,(row+1,col+1)))
            print(f"visited Node {node.val}")
        
        ans = []
        for col in sorted(mp.keys()):
            # Sort by row first, then by value
            ans.append([val for row, val in sorted(mp[col])])

        return ans

        