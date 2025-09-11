# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1, list2 = [], []
        temp_head = head
        while temp_head:
            if temp_head.val < x:
                list1.append(temp_head.val)
            else:
                list2.append(temp_head.val)
            temp_head = temp_head.next

        new_head = ListNode()
        temp = new_head

        for i in list1:
            temp.next = ListNode(i)
            temp = temp.next
        
        for j in list2:
            temp.next = ListNode(j)
            temp = temp.next
        
        return new_head.next

        
            