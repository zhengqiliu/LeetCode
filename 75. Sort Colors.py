class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        index = 0
        while index <= r:
            if nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1
            else:
                nums[l], nums[index] = nums[index], nums[l]
                l += 1
                index += 1
