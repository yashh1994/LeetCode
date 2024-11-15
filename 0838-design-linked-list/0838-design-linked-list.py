class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        i = 0
        root = self.head
        while i < index:
            root = root.next
            if not root.next:
                break 
            i += 1
        if not root.next:
            return -1
        return root.next.val
        

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head

        

    def addAtTail(self, val: int) -> None:
        root = self.head
        while root.next:
            root = root.next
        root.next = Node(val) 
        

    def addAtIndex(self, index: int, val: int) -> None:
        root = self.head
        i = 0
        while i < index:
            root = root.next
            if not root:
                break
            i += 1
        if i == index:
            new_node = Node(val)
            temp = root.next
            root.next = new_node
            new_node.next = temp
        else:
            return


        

    def deleteAtIndex(self, index: int) -> None:
        root = self.head
        i = 0
        while i < index:
            if not root.next:
                break
            root = root.next
            i += 1
        if root.next:
            root.next = root.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)