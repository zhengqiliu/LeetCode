# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
        if left == right:
            return pow(2, left) + self.countNodes(root.right)
        else:
            return pow(2, right) + self.countNodes(root.left)
        
    def findHeight(self, node):
        if not node:
            return 0
        return 1 + self.findHeight(node.left)
