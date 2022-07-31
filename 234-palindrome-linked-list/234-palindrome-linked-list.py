# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# start : 0012 목표시간 30m
# 문제정의 : linkedlist의 val들이 회문이 되는지 확인하라
# input : 1  LinkedList 1e5
# output : true or false
from collections import * 

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # logic
        # 회문의 조건은 ? 앞뒤가 똑같아야 함 단 한글자만 중간에 끼면 괜찮다
        # ex) ababa 일때 -> a기준으로 나눠야함
        
        # easy way -> o(2N) 
        # python의 reversed를 활용 한다.
#         node = head
#         val = []
#         while node != None :
#             val.append(node.val)
#             node = node.next
        
#         return True if val == list(reversed(val)) else False
        node = head
        val_reverse = deque()
        val = []
        while node != None :
            val_reverse.appendleft(node.val)
            val.append(node.val)
            node = node.next
        return True if deque(val) == val_reverse else False 