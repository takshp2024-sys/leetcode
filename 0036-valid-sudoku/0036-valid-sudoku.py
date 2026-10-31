class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track seen digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                    
                # Calculate the 3x3 sub-box index
                box_index = (r // 3) * 3 + (c // 3)
                
                # If the number is already in the row, column, or box, it's invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                    
                # Add the number to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
                
        return True