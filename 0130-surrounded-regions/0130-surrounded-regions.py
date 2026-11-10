class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
            
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            # If out of bounds or not an 'O', stop
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
                
            # Mark this cell as safe by changing it to a temporary character
            board[r][c] = 'S'
            
            # Visit all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # 1. Start DFS from all boundary 'O's to mark safe regions
        # Check top and bottom rows
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
                
        # Check left and right columns
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
                
        # 2. Post-processing: Flip surrounded 'O's to 'X', and restore safe 'S's to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'