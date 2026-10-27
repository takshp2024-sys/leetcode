class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Initialize an m x n grid with all free cells ('.')
        grid = [['.' for _ in range(n)] for _ in range(m)]
        
        # Block off the rest of the grid to force a single path.
        # The only open path will go all the way right along row 0, 
        # and then all the way down along column n-1.
        for r in range(1, m):
            for c in range(n - 1):
                grid[r][c] = '#'
                
        # Join the characters in each row to form strings
        return ["".join(row) for row in grid]