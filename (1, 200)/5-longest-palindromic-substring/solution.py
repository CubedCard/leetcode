class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        
        dp = [[False] * n for _ in range(n)]
        dp[:n] = [[True if i == j else False for j in range(n)] for i in range(n)]
        start, max_len = 0, 1
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 2:
                    dp[i][j] = self.is_palindrome(s[i:j+1])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                
                if dp[i][j] and l > max_len:
                    start = i
                    max_len = l
        
        return s[start:start + max_len]
