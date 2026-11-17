class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Precompute proper divisors for each length
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for mult in range(2 * d, n + 1, d):
                divisors[mult].append(d)
                
        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = float('inf')
                for d in divisors[length]:
                    changes = 0
                    for offset in range(d):
                        l = i + offset
                        r = j - d + 1 + offset
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    min_changes = min(min_changes, changes)
                cost[i][j] = min_changes
                
        # DP table: dp[i][j] = min changes to partition s[0..i] into j parts
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = cost[0][i]
            
        for j in range(2, k + 1):
            for i in range(j - 1, n):
                for m in range(j - 2, i):
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + cost[m + 1][i])
                    
        return dp[n - 1][k]

        