class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list for the graph
        # graph[b] will contain all courses 'a' that depend on 'b'
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
            
        # States: 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited (fully processed)
        state = [0] * numCourses
        
        def dfs(course):
            # If we encounter a node currently in the DFS path, we found a cycle
            if state[course] == 1:
                return False
            # If already fully processed, no cycle found from here
            if state[course] == 2:
                return True
                
            # Mark as visiting
            state[course] = 1
            
            # Visit all dependent courses
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                    
            # Mark as fully processed
            state[course] = 2
            return True
            
        # Check each course to ensure no cycles exist
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
                    
        return True