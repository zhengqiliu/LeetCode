class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(index, target, path):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                if candidates[i] > target:
                    return
                dfs(i+1, target - candidates[i], path + [candidates[i]])
        
        dfs(0, target, [])
        
        return res
