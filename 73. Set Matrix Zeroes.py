class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeros = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for x,y in zeros:
            for i in range(m):
                for j in range(n):
                    matrix[i][y] = 0
                    matrix[x][j] = 0
