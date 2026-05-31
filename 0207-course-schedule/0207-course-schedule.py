class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
            
        queue = [i for i in range(numCourses) if indegree[i] == 0]
        count = 0
        
        for node in queue:
            count += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses

