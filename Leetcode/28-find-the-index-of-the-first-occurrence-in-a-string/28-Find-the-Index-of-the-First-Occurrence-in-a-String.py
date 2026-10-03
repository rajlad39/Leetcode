class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Step 1: Build the LPS array for needle
        m, n = len(needle), len(haystack)
        lps = [0] * m
        prev_lps, i = 0, 1

        while i < m:
            if needle[i] == needle[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        # Step 2: Search needle in haystack using LPS
        i, j = 0, 0  # i for haystack, j for needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]

            if j == m:
                return i - m

        return -1