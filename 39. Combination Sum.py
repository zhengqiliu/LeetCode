class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(candidates, index, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(candidates, i, target - candidates[i], path)
                path.pop()
        
        dfs(candidates, 0, target, [])
        
        return res
