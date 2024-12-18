# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        if size == 0:
            return head
        k = k%size
        temp = head
        for i in range(k):
            temp = temp.next
        left = head
        while temp.next:
            left = left.next
            temp = temp.next
        temp.next = head
        new_head = left.next
        left.next = None
        return new_head

        