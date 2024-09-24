# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def go(node):
            if not node:
                return
            nonlocal ans
            ans[node.val] += 1
            go(node.right)
            go(node.left)
        
        ans = defaultdict(int)
        go(root)
        li = []
        mx = 0
        for k,v in ans.items():
            if mx<v:
                mx = v
                li.clear()
                li.append(k)
            elif mx == v:
                li.append(k)
        return li



        