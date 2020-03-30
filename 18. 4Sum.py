class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        self.findNSum(nums,target, 4, [], res)
        
        return res
        
    def findNSum(self, nums, target, N, path, res):
        if len(nums) < N or N < 2:return
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(path + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        else:
            for i in range(len(nums)-1):
                if target < nums[i]*N or target > nums[-1]*N:break
                if i >= 1 and nums[i] == nums[i-1]:continue
                self.findNSum(nums[i+1:], target-nums[i], N-1, path+[nums[i]], res)
        return
                
                
                
                
                
