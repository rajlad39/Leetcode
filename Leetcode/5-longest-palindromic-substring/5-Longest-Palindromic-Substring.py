class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        start = 0
        max_len = 0

        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After loop ends, valid palindrome range is (left + 1, right - 1)
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd-length palindromes (single center character)
            l1, len1 = expand_around_center(i, i)
            # Even-length palindromes (two-character center)
            l2, len2 = expand_around_center(i, i + 1)

            if len1 > max_len:
                start, max_len = l1, len1
            if len2 > max_len:
                start, max_len = l2, len2

        return s[start:start + max_len]