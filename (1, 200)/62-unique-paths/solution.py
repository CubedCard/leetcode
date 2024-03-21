class Solution(object):
    def uniquePaths(self, m, n):
        if n == 1 and m == 1:
            return 1
        if n <= 0 or m <= 0:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]

class Solution_recursive(object):
    def uniquePaths(self, m, n):
        if n == 1 and m == 1:
            return 1
        if n <= 0 or m <= 0:
            return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

