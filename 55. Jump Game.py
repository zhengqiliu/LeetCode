class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mark = 0
        for i in range(len(nums)):
            if i <= mark:
                mark = max(mark, i + nums[i])
                
        return mark >= len(nums) - 1
