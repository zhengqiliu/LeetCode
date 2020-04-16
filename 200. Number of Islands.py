class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        def dfs(grid, i, j):
            visited.add((i,j))
            for x_, y_ in [(1,0), (0,1), (-1,0),(0,-1)]:
                x, y = i+x_, j+y_
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x, y) in visited or grid[x][y] == '0':
                    continue
                dfs(grid, x, y)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    res += 1
                    dfs(grid, i, j)
        
        return res
                    
        
