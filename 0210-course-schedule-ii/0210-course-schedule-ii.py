from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the adjacency list and in-degree array
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for a, b in prerequisites:
            # b is a prerequisite for a, so there's a directed edge b -> a
            graph[b].append(a)
            in_degree[a] += 1
            
        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        order = []
        
        while queue:
            course = queue.popleft()
            order.append(course)
            
            # Reduce the in-degree of all dependent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If we've processed all courses, return the order; otherwise, there's a cycle
        return order if len(order) == numCourses else []