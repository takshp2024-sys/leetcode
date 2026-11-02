class Solution:
    def totalNQueens(self, n: int) -> int:
        # Sets to track attacked columns and diagonals
        col_set = set()
        pos_diag_set = set()  # (row + col) for anti-diagonals (/)
        neg_diag_set = set()  # (row - col) for main diagonals (\)
        
        count = 0
        
        def backtrack(row: int):
            nonlocal count
            # Base case: If all n queens are placed, we found a valid solution
            if row == n:
                count += 1
                return
                
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the position is under attack
                if col in col_set or (row + col) in pos_diag_set or (row - col) in neg_diag_set:
                    continue
                    
                # Place the queen
                col_set.add(col)
                pos_diag_set.add(row + col)
                neg_diag_set.add(row - col)
                
                # Recurse to the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen's influence
                col_set.remove(col)
                pos_diag_set.remove(row + col)
                neg_diag_set.remove(row - col)
                
        backtrack(0)
        return count