class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        height = [0]*(len(matrix[0]) + 2)
        res = 0
        for row in matrix:
            for i in range(1, len(height)-1):
                height[i] = height[i]+1 if row[i-1] == '1' else 0
            stack = [0]
            for i in range(len(height)):
                while height[stack[-1]] > height[i]:
                    top = stack.pop()
                    res = max(res, height[top] * (i - stack[-1] - 1))
                stack.append(i)
        
        return res
