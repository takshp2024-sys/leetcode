import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Available servers heap: (weight, index)
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)
        
        # Busy servers heap: (free_time, weight, index)
        busy = []
        
        ans = [0] * len(tasks)
        j = 0
        time = 0
        
        while j < len(tasks):
            # 1. Add all tasks that have arrived up to 'time' to the queue
            # But since we don't need a separate queue, we can process them one by one.
            # However, we must ensure we don't assign a task if it hasn't arrived yet.
            
            # If no servers are available, jump to the time when the next server is free
            if not available:
                time = max(time, busy[0][0])
                
            # Free up all servers that are done by 'time'
            while busy and busy[0][0] <= time:
                free_t, w, idx = heapq.heappop(busy)
                heapq.heappush(available, (w, idx))
                
            # If the current task j hasn't arrived yet, we need to wait.
            # But since we process tasks as they are assigned, and tasks arrive at time j,
            # if time < j, we can just jump time to j.
            if time < j:
                time = j
                
            # Assign as many tasks as possible at this second
            # We continue assigning while there is an available server and the task has arrived
            while j < len(tasks) and j <= time and available:
                w, idx = heapq.heappop(available)
                ans[j] = idx
                heapq.heappush(busy, (time + tasks[j], w, idx))
                j += 1
                
            # If we still have tasks remaining and no available servers, 
            # we must wait for a server to become free in the next iteration.
            if j < len(tasks) and not available:
                time = max(time + 1, busy[0][0] if busy else time + 1)
            elif j < len(tasks) and available and j > time:
                time = j
                
        return ans