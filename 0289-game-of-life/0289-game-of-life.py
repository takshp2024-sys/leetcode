class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Directions for the 8 neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                
                # Count live neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # States 1 and 2 were originally live
                        if board[nr][nc] in (1, 2):
                            live_neighbors += 1
                            
                # Apply the rules
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Live to Dead
                else:
                    if live_neighbors == 3:
                        board[r][c] = 3  # Dead to Live
                        
        # Final pass to convert states back to 0 and 1
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1