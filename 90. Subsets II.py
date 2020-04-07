class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def dfs(index, path):
            res.add(tuple(path))
            for i in range(index, len(nums)):
                path += [nums[i]]
                dfs(i+1, path)
                path.pop()
        
        dfs(0, [])
        return list(map(list, res))
