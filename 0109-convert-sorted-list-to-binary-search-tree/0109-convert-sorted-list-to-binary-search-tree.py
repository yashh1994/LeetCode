# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def go(li):
            if not li:
                return None
            index = len(li)//2
            node = TreeNode(li[index])
            node.left = go(li[:index])
            node.right = go(li[index+1:])
            return node
        li = []
        while head:
            li.append(head.val)
            head = head.next
        ans = go(li)
        return ans
        