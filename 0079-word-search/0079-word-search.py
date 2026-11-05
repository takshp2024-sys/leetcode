class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def backtrack(r: int, c: int, index: int) -> bool:
            # Base case: If we have matched all characters of the word
            if index == len(word):
                return True
                
            # Boundary checks and character match check
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[index]:
                return False
                
            # Mark the cell as visited by temporarily changing its value
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 adjacent directions
            found = (backtrack(r + 1, c, index + 1) or
                     backtrack(r - 1, c, index + 1) or
                     backtrack(r, c + 1, index + 1) or
                     backtrack(r, c - 1, index + 1))
                     
            # Backtrack: restore the cell's original value
            board[r][c] = temp
            
            return found
            
        # Start a DFS from every cell that matches the first character
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
                        
        return False