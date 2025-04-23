# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses 
        
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nei in graph[node]:  
                indegree[nei] -= 1   
                if indegree[nei] == 0:
                    queue.append(nei)
        if len(order) == numCourses:
            return order
        else:
            return []
