# Solution 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[-1][-1]

    
# Solution 2
# Math Solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        left = m-1
        right = n-1
        
        def factorial(n):
            if n == 0:
                return 1
            s = 1
            while n > 1:
                s *= n
                n -= 1
            
            return s
        
        return factorial(left + right) // (factorial(left) * factorial(right))
        
