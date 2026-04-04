# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        nextNode = head
        while nextNode is not None:
            print(nextNode)
            temp = nextNode.next
            nextNode.next = current
            current = nextNode
            nextNode = temp
        
        return current
        