class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        sum = set()
        diff = set()
        
        def dfs(path):
            if len(path) == n:
                self.res += 1
                return
            row = len(path)
            for i in range(n):
                if i not in path and i + row not in sum and i - row not in diff:
                    sum.add(i+row)
                    diff.add(i-row)
                    path.append(i)
                    dfs(path)
                    path.pop()
                    sum.remove(i+row)
                    diff.remove(i-row)
        dfs([])
        
        return self.res
