class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        res = []
        def dfs(nums, path, s, k, target):
            if len(path) == k:
                if s == target:
                    res.append(path)
                return
            if not nums:
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], s + nums[i], k, target)
        
        dfs(nums, [], 0, k, n)
        
        return res
