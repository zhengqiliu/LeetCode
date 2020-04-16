# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = {}
        def dfs(node, depth):
            if not node:
                return
            if depth not in res:
                res[depth] = node
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return [res[i].val for i in range(len(res))]
