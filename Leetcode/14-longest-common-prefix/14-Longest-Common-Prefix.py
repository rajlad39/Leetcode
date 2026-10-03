class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Scan characters column by column
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for string in strs[1:]:
                # If i is out of bounds or character doesn't match
                if i == len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]