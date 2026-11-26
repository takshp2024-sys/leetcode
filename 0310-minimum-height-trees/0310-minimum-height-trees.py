from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case: if there's only 1 node, it's the root
        if n == 1:
            return [0]
            
        # Build the graph adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # Find the initial leaves (nodes with only 1 connection)
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        remaining_nodes = n
        
        # Peel off leaves layer by layer until 1 or 2 nodes remain
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                # Remove the leaf from its neighbor's adjacency list
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    # If the neighbor becomes a leaf, add it to the queue
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
                        
        # The remaining nodes in the queue are the centers (MHT roots)
        return list(leaves)