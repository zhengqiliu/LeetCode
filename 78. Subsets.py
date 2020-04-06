class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, index, path):
            res.append(list(path))
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(nums, i+1, path)
                path.pop()
        
        dfs(nums, 0, [])
        return res
