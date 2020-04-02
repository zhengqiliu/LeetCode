class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = None
        maximum = -float('inf')
        for num in nums:
            if not s:
                s = num
            else:
                s += num
            maximum = max(maximum, s)
            if s < 0:
                s = None

        return maximum
