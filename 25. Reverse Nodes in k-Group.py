# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k <= 1:
            return head
        
        def reverse(l,r):
            res = cur = l.next
            prev = l
            while cur != r:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            l.next = prev
            res.next = r
            
            return res
        
        dummy = ListNode(0)
        dummy.next = head
        begin = dummy
        count = 0
        while head:
            count += 1
            if count < k:
                head = head.next
            else:
                begin = reverse(begin,head.next)
                head = begin.next
                count = 0
            
        return dummy.next
        
        
        
        
        
        
        
        
            
