# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)
        def go(node):
            if not node:
                return 0
            nonlocal mp
            sm = node.val+go(node.left)+go(node.right)
            mp[sm] += 1
            return sm
        go(root)
        ans = []
        mx = 0
        for k,v in mp.items():
            if v > mx:
                ans.clear()
                ans.append(k)
                mx = v
            elif v == mx:
                ans.append(k)
        return ans

        