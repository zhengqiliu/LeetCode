class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        def dfs(nums, index, path, k):
            if len(path) == k:
                res.append(path)
                return
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                dfs(nums, i+1, path+[nums[i]], k)
        
        dfs(nums, 0, [], k)
        
        return res
