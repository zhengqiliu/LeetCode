# Solution 1
class Solution:
    def trap(self, height: List[int]) -> int:
        #(index, height)
        left_max = height[:]
        right_max = height[:]
        
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1], left_max[i])
            
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i], right_max[i+1])
        
        res = 0
        for i in range(len(height)):
            res += min(left_max[i], right_max[i]) - height[i]
        
        return res
        
# Solution 2
class Solution:
    def trap(self, height: List[int]) -> int:
        #(index, height)
        res = 0
        stack = []
        i = 0
        while i < len(height):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - height[top]
                res += distance * h

            stack.append(i)
            i += 1
        
        return res
     
# Solution 3
