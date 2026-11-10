"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        # Dictionary to map original nodes to their clones
        old_to_new = {}
        
        def dfs(curr_node):
            # If the node is already cloned, return its clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            # Create a new clone for the current node
            clone = Node(curr_node.val)
            old_to_new[curr_node] = clone
            
            # Recursively clone all neighbors and add them to the clone's neighbors list
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)