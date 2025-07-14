# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        monotonic_stack = []
        if not head:
            return head
        while head is not None:
            if monotonic_stack:
                if monotonic_stack[-1]>=head.val:
                    monotonic_stack.append(head.val)
                else:
                    while monotonic_stack and monotonic_stack[-1]<head.val:
                        monotonic_stack.pop()
                    monotonic_stack.append(head.val)

            else:
                monotonic_stack.append(head.val)
            head = head.next
        
        new_head = None
        while monotonic_stack:
            print(monotonic_stack[-1])
            node_val = monotonic_stack.pop()
            node = ListNode()
            node.val = node_val
            node.next = new_head
            new_head = node

        return new_head


