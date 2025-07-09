# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        current = prev.next
        while prev.next:
            prev.val = current.val
            if not current.next:
                prev.next = None
                return
            prev = prev.next
            current = current.next
        return 
        