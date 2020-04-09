# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        def build(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left = build(nums[:mid])
            node.right = build(nums[mid+1:])
            
            return node
        
        return build(array)
            
            
            
            
            
            
            
            
            
            
            
