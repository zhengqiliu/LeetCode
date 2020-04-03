# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head and not head.next:
            return head
        end = head
        anc = {}
        prev = None
        length = 1
        while end and end.next:
            length += 1
            anc[end] = prev
            prev = end
            end = end.next
        anc[end] = prev
        k %= length
        while k > 0:
            end.next = head
            head = end
            anc[end].next = None
            end = anc[end]
            k -= 1
        
        return head
