class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sum = set()
        diff = set()
        res = []
        
        def dfs(path):
            if len(path) == n:
                res.append(draw(path))
                return
            row = len(path)
            for i in range(n):
                if i not in path and i + row not in sum and i - row not in diff:
                    path.append(i)
                    sum.add(i+row)
                    diff.add(i-row)
                    dfs(path)
                    path.pop()
                    sum.remove(i+row)
                    diff.remove(i-row)
        
        def draw(path):
            return ['.'*i + 'Q' + '.'*(n-1-i) for i in path]
        
        dfs([])
        
        return res
