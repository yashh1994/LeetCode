class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        lst = []
        temp = head
        
        while temp is not None:
            lst.append(temp.val)
            temp = temp.next
        
        extra = len(lst) % k
        ans = []
        share = len(lst) // k
        
        # Create the split linked list parts
        for i in range(k):
            l = []
            for j in range(share):
                if head is not None:
                    l.append(head.val)
                    head = head.next
            if i < extra:
                if head is not None:
                    l.append(head.val)
                    head = head.next

            if l:
                part_head = ListNode(l[0])
                current = part_head
                for value in l[1:]:
                    current.next = ListNode(value)
                    current = current.next
                ans.append(part_head)
            else:
                ans.append(None)
        
        return ans