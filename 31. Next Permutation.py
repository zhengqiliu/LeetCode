class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                mark = i-1
                minDiff = float('inf')
                minDiffIndex = 0
                for j in range(mark, len(nums)):
                    if nums[j] > nums[mark]:
                        if nums[j] - nums[mark] <= minDiff:
                            minDiff = nums[j] - nums[mark]
                            minDiffIndex = j
                nums[mark], nums[minDiffIndex] = nums[minDiffIndex], nums[mark]
                
                nums[(mark+1):] = reversed(nums[(mark+1):])
                return
        nums[:] = reversed(nums)
        return
