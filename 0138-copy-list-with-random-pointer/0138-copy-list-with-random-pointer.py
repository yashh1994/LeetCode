class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {}
        temp = head

        ans = Node(-1)
        dummy = ans

        while temp:
            if temp not in mp:
                mp[temp] = Node(temp.val)
            dummy.next = mp[temp]
            if temp.next:
                if temp.next not in mp:
                    mp[temp.next] = Node(temp.next.val)
                dummy.next.next = mp[temp.next]
            if temp.random:
                if temp.random not in mp:
                    mp[temp.random] = Node(temp.random.val)
                dummy.next.random = mp[temp.random]
            temp = temp.next
            dummy = dummy.next

        return ans.next
