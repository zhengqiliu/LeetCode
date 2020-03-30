class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        minDiff = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:continue
            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                diff = total - target
                if abs(diff) < minDiff:
                    minDiff = abs(diff)
                    res = total
                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    return total
        
        return res
