class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, char in enumerate(s, 1):
            # Reversed alphabet position: 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            total += rev_alphabet_pos * i
        return total