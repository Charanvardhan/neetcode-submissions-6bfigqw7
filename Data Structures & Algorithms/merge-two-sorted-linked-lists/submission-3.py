# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        # if first is None:
        #     return second
        # if second is None:
        #     return first
        
        head = ListNode()
        itr = head
        
        
        while first and second:
            if first.val >= second.val:
                itr.next = second
                second = second.next
            else:
                itr.next = first
                first = first.next
            itr = itr.next
            
        while second:
            itr.next = second
            second = second.next
            itr = itr.next
        
        while first:
            itr.next = first
            first = first.next
            itr = itr.next
        
        return head.next
            
        