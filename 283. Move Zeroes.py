class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        slow, fast = 0, 1
        while slow < fast and fast < len(nums):
            if nums[slow] == 0 and nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] == 0 and nums[fast] == 0:
                fast += 1
                continue
            fast += 1
            slow += 1
