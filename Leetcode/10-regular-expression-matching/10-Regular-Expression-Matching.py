class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, .* that match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # Case 1: Match 0 instances of preceding character
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: Match 1 or more instances if character matches
                    first_match = s[i - 1] == p[j - 2] or p[j - 2] == '.'
                    if first_match:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    first_match = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                    if first_match:
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]