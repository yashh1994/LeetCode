# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        i = 0
        while i < n:
            temp = temp.next
            i += 1
        if not temp:
            return head.next
        
        fast = temp
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        node_d = slow.next
        slow.next = slow.next.next
        node_d = None
        return head
        

        