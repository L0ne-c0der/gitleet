# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #no need for array
        #create two linked lists, and add low and higher values accordingly
        #just change the routes by erasing current next
        #no need to create new nodes

        slist , blist = ListNode(), ListNode()
        small , big = slist, blist

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            
            head = head.next
    
        small.next = blist.next
        big.next = None

        return slist.next
        

            

        
            