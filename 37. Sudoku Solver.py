class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(x, y, c):
            for i in range(9):
                if board[i][y] == c:return False
                if board[x][i] == c:return False
            x ,y = x-x%3, y-y%3
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] == c:
                        return False
                    
            return True
        
        def solver(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for c in range(1, 10):
                            c = str(c)
                            if isValid(i, j, c):
                                board[i][j] = c
                                if solver(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        
        solver(board)
