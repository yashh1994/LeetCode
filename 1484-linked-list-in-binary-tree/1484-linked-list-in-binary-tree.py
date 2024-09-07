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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def is_same(head:Optional[ListNode],node:Optional[TreeNode]) -> bool:
            if not head:
                return True
            if not node or head.val != node.val:
                return False
            return is_same(head.next,node.left) or is_same(head.next,node.right)
        
        ans = False
        qe = []
        qe.append(root)
        while qe:
            si = len(qe)
            for i in range(si):
                n = qe.pop(0)
                if is_same(head,n):
                    return True
                if n.left:
                    qe.append(n.left)
                if n.right:
                    qe.append(n.right)
        return False




        