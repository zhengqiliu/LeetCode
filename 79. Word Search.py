class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        self.res = False
        def dfs(board, word, i, j):
            if self.res:
                return
            if board[i][j] == word[0]:
                if len(word) == 1:
                    self.res = True
                    return
                visited.add((i,j))
                for x_, y_ in [(0,1), (1,0), (-1,0), (0,-1)]:
                    x, y = i+x_, j+y_
                    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x,y) in visited:
                        continue
                    dfs(board, word[1:], x, y)
                visited.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, word, i, j)

        return self.res
