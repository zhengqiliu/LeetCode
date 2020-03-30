# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solition1
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        def mergeTwo(l1,l2):
            dummy = cur = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            
            return dummy.next
        while len(lists) >= 2:
            l1 = lists.pop()
            l2 = lists.pop()
            merged = mergeTwo(l1,l2)
            lists.append(merged)
        
        return lists[0]
        
        
# Solution2
# With heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        list2index = {}
        for l in lists:
            if l:
                list2index[l] = len(list2index)
                
        dummy = cur = ListNode(0)
        heap = []
        for l in lists:
            if l:
                heappush(heap, (l.val, list2index[l], l))
        
        while heap:
            _, id, node = heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heappush(heap, (node.val, id, node))
            
        return dummy.next
            
            
            
            
            
