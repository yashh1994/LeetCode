"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_vals = []

        def create_linked_list(values):
            if not values:
                return None
            
            head = Node(values[0])
            current = head

            for val in values[1:]:
                new_node = Node(val)
                current.next = new_node
                new_node.prev = current
                current = new_node
            
            return head  
        def go(node):
            if not node:
                return
            nonlocal node_vals
            node_vals.append(node.val) 
            if node.child:
                go(node.child)  
            go(node.next) 

        go(head)
        print(node_vals)
        return create_linked_list(node_vals)       