import sys
sys.setrecursionlimit(200000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # 1. Build the Adjacency List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        parent = [-1] * n
        depth = [0] * n
        size = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        
        # 2. First DFS (Iterative to avoid recursion limit/overhead)
        stack = [(0, -1, 0, False)]
        while stack:
            u, p, d, visited = stack.pop()
            if visited:
                size[u] = 1
                max_size = 0
                for v in adj[u]:
                    if v != p:
                        size[u] += size[v]
                        if size[v] > max_size:
                            max_size = size[v]
                            heavy[u] = v
            else:
                parent[u] = p
                depth[u] = d
                stack.append((u, p, d, True))
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, d + 1, False))
                        
        # 3. Second DFS for HLD pos assignment
        current_pos = 0
        stack = [(0, 0)]
        while stack:
            u, h = stack.pop()
            # Traverse the heavy path iteratively
            while u != -1:
                head[u] = h
                pos[u] = current_pos
                current_pos += 1
                
                # Push light children to stack
                for v in adj[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))
                
                # Move to heavy child
                u = heavy[u]
                
        # 4. Iterative Segment Tree for XOR
        tree_size = 1
        while tree_size < n:
            tree_size <<= 1
        seg_tree = [0] * (2 * tree_size)
        
        def get_mask(c):
            return 1 << (ord(c) - ord('a'))
            
        # Build the segment tree
        for i in range(n):
            seg_tree[tree_size + pos[i]] = get_mask(s[i])
            
        for i in range(tree_size - 1, 0, -1):
            seg_tree[i] = seg_tree[2 * i] ^ seg_tree[2 * i + 1]
            
        # Segment Tree Point Update
        def update_tree(idx, val):
            idx += tree_size
            seg_tree[idx] = val
            idx >>= 1
            while idx > 0:
                seg_tree[idx] = seg_tree[2 * idx] ^ seg_tree[2 * idx + 1]
                idx >>= 1
                
        # Segment Tree Range Query
        def query_tree(l, r):
            res = 0
            l += tree_size
            r += tree_size + 1
            while l < r:
                if l & 1:
                    res ^= seg_tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    res ^= seg_tree[r]
                l >>= 1
                r >>= 1
            return res
            
        # Query Path XOR
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                res ^= query_tree(pos[head[u]], pos[u])
                u = parent[head[u]]
                
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= query_tree(pos[u], pos[v])
            return res

        # 5. Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                new_mask = get_mask(c)
                # We update regardless to avoid costly string/char lookups
                update_tree(pos[u], new_mask)
                # Note: we don't strictly need to update 's' array if we only rely on seg_tree
            elif parts[0] == "query":
                u = int(parts[1])
                v = int(parts[2])
                mask = query_path(u, v)
                if mask == 0 or (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
                    
        return ans