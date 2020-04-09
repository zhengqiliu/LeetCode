# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
            
        first, second = prev, cur
        while n > 0:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        
        if first:
            first.next = prev
        else:
            head = prev
        second.next = cur
        
        return head
        
        
        
