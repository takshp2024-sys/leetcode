class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        
        # Sets to keep track of attacked columns and diagonals
        col_set = set()
        pos_diag_set = set()  # (row + col) identifies the anti-diagonal (/) direction
        neg_diag_set = set()  # (row - col) identifies the main diagonal (\) direction
        
        # Board represented as a 2D grid of '.'
        board = [["."] * n for _ in range(n)]
        
        def backtrack(row: int):
            # Base case: If we placed queens in all n rows, we found a valid solution
            if row == n:
                # Convert the 2D board into a list of strings
                result.append(["".join(r) for r in board])
                return
                
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if this column or either diagonal is already under attack
                if col in col_set or (row + col) in pos_diag_set or (row - col) in neg_diag_set:
                    continue
                    
                # Place the queen
                board[row][col] = "Q"
                col_set.add(col)
                pos_diag_set.add(row + col)
                neg_diag_set.add(row - col)
                
                # Recurse to the next row
                backtrack(row + 1)
                
                # Backtrack: Remove the queen and free up the column/diagonals
                board[row][col] = "."
                col_set.remove(col)
                pos_diag_set.remove(row + col)
                neg_diag_set.remove(row - col)
                
        backtrack(0)
        return result