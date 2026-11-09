import heapq

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1  # All servers are initially available
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node, start, mid, idx, val)
            else:
                self.update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return -1
        if l <= start and end <= r:
            if self.tree[node] == 0:
                return -1
            if start == end:
                return start
        mid = (start + end) // 2
        res = self.query(2 * node, start, mid, l, r)
        if res != -1:
            return res
        return self.query(2 * node + 1, mid + 1, end, l, r)

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Segment tree to track available servers (1 = available, 0 = busy)
        seg_tree = SegmentTree(k)
        
        # Min-heap for busy servers: (free_time, server_id)
        busy = []
        
        # Count of requests handled by each server
        count = [0] * k
        
        for i in range(len(arrival)):
            time = arrival[i]
            
            # Free up servers that have completed their tasks by 'time'
            while busy and busy[0][0] <= time:
                _, server = heapq.heappop(busy)
                seg_tree.update(1, 0, k - 1, server, 1)
                
            # Find the preferred server
            target = i % k
            
            # Try to find an available server starting from 'target' to the end
            server = seg_tree.query(1, 0, k - 1, target, k - 1)
            
            # If not found, wrap around and search from 0 to 'target - 1'
            if server == -1:
                server = seg_tree.query(1, 0, k - 1, 0, target - 1)
                
            # If a server is found, assign the request
            if server != -1:
                count[server] += 1
                seg_tree.update(1, 0, k - 1, server, 0) # Mark as busy
                heapq.heappush(busy, (time + load[i], server))
                
        # Find the maximum number of requests handled
        max_req = max(count)
        
        # Return all servers that handled the maximum number of requests
        return [i for i in range(k) if count[i] == max_req]