class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        ans = s  # Default initial candidate

        for k in range(1, n + 1):
            # 1. Reverse the first k characters
            prefix_rev = s[:k][::-1] + s[k:]
            if prefix_rev < ans:
                ans = prefix_rev

            # 2. Reverse the last k characters
            suffix_rev = s[:n - k] + s[n - k:][::-1]
            if suffix_rev < ans:
                ans = suffix_rev

        return ans