# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def go(li):
            if not li:
                return None
            index = len(li)//2
            node = TreeNode(li[index])
            node.left = go(li[:index])
            node.right = go(li[index+1:])
            return node

        index = len(nums)//2
        ans = TreeNode(nums[index])
        ans.right = go(nums[index+1:])
        ans.left = go(nums[:index])
        return ans
    

        