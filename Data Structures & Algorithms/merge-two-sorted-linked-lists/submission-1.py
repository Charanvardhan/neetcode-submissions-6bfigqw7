# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        crtTop = list1
        crtBot = list2

        if crtTop is None:
            return crtBot
        
        if crtBot is None:
            return crtTop
        
        if crtTop.val < crtBot.val:
            current = crtTop 
            crtTop = crtTop.next
        else:
            current = crtBot
            crtBot = crtBot.next

        temp = current

        while crtTop and crtBot:
            
            if crtTop.val > crtBot.val:
                temp.next = crtBot
                crtBot = crtBot.next
            else:
                temp.next = crtTop
                crtTop = crtTop.next

            temp = temp.next
            # print(crtTop.val, .val)

        if not crtTop:
            temp.next = crtBot
        
        else:
            temp.next = crtTop

        return current
        