class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize sets to track the numbers present in rows, cols, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Populate the sets with initial numbers and record empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))
                    
        def backtrack(index):
            # Base case: if all empty cells are filled, we are done
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits '1' to '9'
            for num in map(str, range(1, 10)):
                # Check if the number is valid in the current row, col, and box
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)
                    
                    # Recursively try to solve the rest of the board
                    if backtrack(index + 1):
                        return True
                        
                    # If placing the number didn't lead to a solution, backtrack (undo)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)
                    
            # If no digit from 1-9 can be placed, return False to trigger backtracking
            return False
            
        # Start the backtracking from the first empty cell
        backtrack(0)