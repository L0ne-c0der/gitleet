# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _swapPairs(current):
            if not current or not current.next:
                return current
            later = _swapPairs(current.next.next)
            after = current.next
            current.next = later
            after.next = current
            return after
        
        return _swapPairs(head)
            
