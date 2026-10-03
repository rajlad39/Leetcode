class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            # If the character is already in the current window, move 'left'
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Store/update the character's last seen index
            char_map[char] = right
            
            # Update maximum length found so far
            max_len = max(max_len, right - left + 1)

        return max_len