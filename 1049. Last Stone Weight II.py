class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        dp = [False] * (sum_stones + 1)
        dp[0] = True
        for s in stones:
            for i in range(sum_stones, s-1, -1):
                dp[i] = dp[i] or dp[i-s]
        
        for i in range(sum_stones // 2, -1, -1):
            if dp[i]:return(sum_stones - i - i)
        
        return 0
