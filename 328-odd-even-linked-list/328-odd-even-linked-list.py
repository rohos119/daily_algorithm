# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        end = head
        size = 0
        
        while end.next:
            end = end.next
            size += 1
        
        jumps = (size // 2)+1 if size & 1 else (size // 2)
        curr ,ans = head, head
        while jumps:
            end.next = curr.next
            curr.next = curr.next.next
            end.next.next = None
            curr = curr.next
            end = end.next
            jumps -= 1
			
        return head
        