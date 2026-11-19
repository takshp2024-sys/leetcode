class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the end node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of the word
            
        m, n = len(board), len(board[0])
        result = []
        
        # Step 2: DFS Backtracking
        def dfs(r, c, node):
            char = board[r][c]
            
            # If the character exists in the current Trie node's children
            if char in node.children:
                next_node = node.children[char]
                
                # If we reached the end of a word
                if next_node.word:
                    result.append(next_node.word)
                    # Set to None to avoid adding duplicate words (if the same word can be formed)
                    next_node.word = None
                    
                # Mark the cell as visited
                board[r][c] = '#'
                
                # Explore neighbors
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                        dfs(nr, nc, next_node)
                        
                # Backtrack: unmark the cell
                board[r][c] = char
                
                # Optimization: Prune the Trie to remove dead ends
                if not next_node.children:
                    del node.children[char]
                    
        # Step 3: Start DFS from every cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
                
        return result