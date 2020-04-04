class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        direction = [(0,1), (1,0), (0, -1), (-1,0)]
        index = 0
        visited = set()
        cur = (0, 0)
        for i in range(1, n**2 + 1):
            x, y = cur
            visited.add((x, y))
            res[x][y] = i
            x_, y_ = x + direction[index][0], y + direction[index][1]
            if 0 <= x_ < n and 0 <= y_ < n and (x_, y_) not in visited:
                cur = (x_, y_)
            else:
                index += 1
                index = index % 4
                cur = (x+direction[index][0], y + direction[index][1])
        
        return res
                            
        
