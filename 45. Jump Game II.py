class Solution:
    def jump(self, nums: List[int]) -> int:
        end = farthest = 0
        jumps = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                end = farthest
                jumps += 1
                
        return jumps
