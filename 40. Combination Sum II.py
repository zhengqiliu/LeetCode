class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        def dfs(index, target, path):
            if target < 0:
                return
            if target == 0:
                res.add(tuple(path))
                return
            for i in range(index, len(candidates)):
                dfs(i+1, target - candidates[i], path + [candidates[i]])
        
        dfs(0, target, [])
        
        return list(res)
