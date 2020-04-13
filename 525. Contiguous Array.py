class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dic = {0:-1}
        cnt = res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt in dic:
                res = max(res, i - dic[cnt])
            else:
                dic[cnt] = i
        
        return res
