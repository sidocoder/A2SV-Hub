# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        preq = [[False] * numCourses for _ in range(numCourses)]

        
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
            preq[u][v] = True  

        
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                
                for i in range(numCourses):
                    if preq[i][curr]: 
                        preq[i][neighbor] = True
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        
        ans = []
        for u, v in queries:
            ans.append(preq[u][v])

        return ans
