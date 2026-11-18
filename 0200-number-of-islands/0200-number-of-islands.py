class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or the cell is water ('0'), stop
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
                
            # Mark the current land cell as visited by setting it to '0'
            grid[r][c] = '0'
            
            # Recursively visit all 4 adjacent directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(m):
            for c in range(n):
                # If we find a piece of land, it's a new island
                if grid[r][c] == '1':
                    num_islands += 1
                    # Sink the entire island using DFS
                    dfs(r, c)
                    
        return num_islands