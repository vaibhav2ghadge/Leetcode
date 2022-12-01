# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        while second and second.next:
            
            first = first.next
            
            if not second.next.next:
                return first
            
            second = second.next.next
            
        return first.next
        