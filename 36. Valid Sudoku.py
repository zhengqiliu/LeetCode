class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkRow(line):
            nums = set()
            for num in line:
                if num != ".":
                    if num in nums:
                        return False
                    nums.add(num)
            
            return True
        
        for line in board:
            if not checkRow(line):
                return False
        
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            if not checkRow(temp):
                return False
        
        
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                temp = [board[x][y] for x in range(i,i+3) for y in range(j, j+3)]
                if not checkRow(temp):
                    return False
        
        return True
                
                
                
                
                
                
                
