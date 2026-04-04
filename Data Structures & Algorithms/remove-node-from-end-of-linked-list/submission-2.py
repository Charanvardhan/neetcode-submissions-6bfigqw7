# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        end = dummy               
        start = dummy 
        while n > 0:
            end = end.next
            n -= 1

        while end and end.next:
            end = end.next
            start = start.next
        

        start.next = start.next.next
        
        return dummy.next