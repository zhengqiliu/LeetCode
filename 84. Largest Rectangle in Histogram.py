class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [-1]
        heights += [0]
        for i in range(len(heights)):
            while heights[stack[-1]] > heights[i]:
                index = stack.pop()
                res = max(res, heights[index] * (i - stack[-1] - 1))
            stack.append(i)
        return res
