class ListNode:
    
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        head = self.head
        for i in range(index):
            head = head.next
        return head.val
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node

        if not self.tail:
            self.tail = self.head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return
        
        if index==0:
            self.addAtHead(val)
            return
        
        count = 0
        head = self.head
        while count < (index-1):
            head = head.next
            count+=1

        next_node = head.next
        head.next = ListNode(val, next_node)
        self.size+=1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        head = self.head
        if index == 0:
            self.head = head.next
            self.size-=1
            return
        
        count = 0
        while count < (index - 1):
            head = head.next
            count+=1

        if index == self.size - 1:
            head.next = None
            self.tail = head
            self.size-=1
            return

        head.next = head.next.next
        self.size-=1
        return            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)