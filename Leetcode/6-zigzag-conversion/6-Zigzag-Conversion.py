class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char
            
            # Change direction when hitting top or bottom row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
                
            curr_row += 1 if going_down else -1

        return "".join(rows)