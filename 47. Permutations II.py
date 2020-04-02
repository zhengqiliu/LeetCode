# Solution 1
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(nums, path):
            if not nums:
                res.add(tuple(path))
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
        
        dfs(nums, [])
        
        return list(res)
    
    
# Solution 2
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(path, counter):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for x in counter:
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    dfs(path, counter)
                    path.pop()
                    counter[x] += 1
        
        dfs([], Counter(nums))
        
        return res
        
