# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set()
        for n in nums:
            numSet.add(n)
        ans = ListNode(0)
        temp = ans
        while head is not None:
            if head.val not in numSet:
                temp.next = head
                temp = temp.next
            head = head.next
        temp.next = None
        return ans.next
            