class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If there's only 1 row or the string fits in one row, no change is needed
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array of strings for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            # Append the current character to the current row
            rows[current_row] += char
            
            # If we hit the top or bottom row, reverse direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move to the next row based on the current direction
            if going_down:
                current_row += 1
            else:
                current_row -= 1

        # Join all the rows together to form the final string
        return "".join(rows)