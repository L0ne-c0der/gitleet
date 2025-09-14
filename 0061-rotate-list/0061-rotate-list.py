# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #using an array
        if not head or not head.next:
            return head
        
        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        size = len(arr)
        new_arr = [0] * size

        for i in range(size):
            new_arr[(i+k)%size] = arr[i]
        
        new_head = ListNode()
        temp = new_head

        for num in new_arr:
            temp.next = ListNode(num)
            temp = temp.next
        
        return new_head.next

        
        


