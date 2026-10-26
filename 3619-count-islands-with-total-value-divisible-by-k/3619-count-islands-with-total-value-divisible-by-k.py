class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Base case: out of bounds or water (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            # Get the current cell's value and mark it as visited by setting to 0
            val = grid[r][c]
            grid[r][c] = 0
            
            # Recursively sum up all 4-directionally connected land cells
            return (val + dfs(r + 1, c) + 
                         dfs(r - 1, c) + 
                         dfs(r, c + 1) + 
                         dfs(r, c - 1))

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find unvisited land, it's a new island
                if grid[r][c] > 0:
                    total_value = dfs(r, c)
                    # Check if the island's total value is divisible by k
                    if total_value % k == 0:
                        count += 1
                        
        return count