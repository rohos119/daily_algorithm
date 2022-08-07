# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ret = result = head
        sets = []
        while head:
            sets.append(head.val)
            head = head.next
        sets = sorted(sets)
        counter = 0
        while result:
            result.val = sets[counter]
            counter += 1
            result = result.next
        return ret
        