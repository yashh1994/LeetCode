from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            if not node:
                return "#"
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[serial] += 1
            if count[serial] == 2:  # Only add once when duplicate is found
                duplicates.append(node)
            return serial

        count = defaultdict(int)
        duplicates = []
        serialize(root)
        return duplicates
