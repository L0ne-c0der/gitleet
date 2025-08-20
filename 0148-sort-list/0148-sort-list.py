# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        arr.sort()
        new_head = ListNode()
        temp = new_head
        for num in arr:
            node = ListNode()
            node.val = num
            new_head.next = node
            new_head = new_head.next
        return temp.next