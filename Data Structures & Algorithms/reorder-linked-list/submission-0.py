# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        current = None
        reverse = slow.next
        slow.next = None
        while reverse:
            temp = reverse.next
            reverse.next = current
            current = reverse
            reverse = temp
        
        l1 = head
        l2 = current

        while l2:
            l1temp = l1.next
            l1.next = l2
            l1 = l1temp
            l2temp = l2.next
            l2.next = l1
            l2 = l2temp
        

