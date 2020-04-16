class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        prev = None
        use = not_use = 0
        for k in sorted(cnt):
            if k-1 == prev:
                use, not_use = k*cnt[k] + not_use, max(not_use, use)
            else:
                use, not_use = k*cnt[k] + max(not_use, use), max(not_use, use)
            prev = k
        
        return max(not_use, use)
