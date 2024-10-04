# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = set()
        while head:
            if head in li:
                return head
            li.add(head)
            head = head.next
        return None
        