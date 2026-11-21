import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        
        # Build the original tree adjacency list
        for i in range(1, n):
            children[parent[i]].append(i)
            
        # Dictionary to keep track of the closest ancestor for each character
        last_seen = {}
        new_parent = list(parent)
        
        # DFS to find the new parent for each node
        def dfs_find_parent(node):
            char = s[node]
            
            # If there's an ancestor with the same character, it becomes the new parent
            if char in last_seen:
                new_parent[node] = last_seen[char]
                
            # Save the old state so we can backtrack correctly
            old_val = last_seen.get(char)
            last_seen[char] = node
            
            for child in children[node]:
                dfs_find_parent(child)
                
            # Backtrack: restore the previous closest ancestor for this character
            if old_val is not None:
                last_seen[char] = old_val
            else:
                del last_seen[char]
                
        dfs_find_parent(0)
        
        # Build the new tree based on updated parents
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
            
        ans = [1] * n
        
        # DFS to calculate subtree sizes in the new tree
        def dfs_subtree_size(node):
            size = 1
            for child in new_children[node]:
                size += dfs_subtree_size(child)
            ans[node] = size
            return size
            
        dfs_subtree_size(0)
        return ans