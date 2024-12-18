# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            pre = None
            cur = head
            nxt = cur.next
            while cur != None:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next if nxt else None
            return pre
        temp = head
        check = False
        prev = None
        while temp != None:
            kth = temp
            nxt = kth.next
            for i in range(k-1):
                if kth == None:
                    break
                kth = kth.next
                nxt = nxt.next if nxt else None 
            if kth:
                kth.next = None
                new_h = reverse(temp)
                if not check:
                    head = kth
                    check = True
                if prev:
                    prev.next = new_h
                prev = temp
                
            else:
                prev.next = temp
                return head
            temp= nxt
        return head
            


        