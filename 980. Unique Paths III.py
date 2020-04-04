class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        structures = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == -1:
                    structures += 1
        target_steps = len(grid)*len(grid[0]) - structures -1
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(grid, x, y, step):
            if grid[x][y] == 2:
                if step == target_steps:
                    self.res += 1
                return
            visited.add((x,y))
            for a, b in directions:
                x_, y_ = x+a, y+b
                if 0<=x_<len(grid) and 0<=y_<len(grid[0]) and (x_,y_) not in visited and grid[x_][y_] != -1:
                    dfs(grid, x_, y_, step+1)
            visited.remove((x,y))
        
        dfs(grid, start[0], start[1],0)
        
        return self.res
