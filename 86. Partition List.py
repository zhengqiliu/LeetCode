# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_big = big = ListNode(0)
        dummy_small = small = ListNode(0)
        while head:
            if head.val >= x:
                big.next = head
                big = big.next
            else:
                small.next = head
                small = small.next
            head = head.next
        small.next = dummy_big.next
        big.next = None
        
        return dummy_small.next
        
