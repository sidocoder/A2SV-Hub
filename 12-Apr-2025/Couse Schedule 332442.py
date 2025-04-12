# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        colors = [-1] * numCourses  # -1 = unvisited, 1 = visiting, 2 = visited

        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(node):
            if colors[node] == 1:
                return False  # cycle detected
            if colors[node] == 2:
                return True   # already visited and no cycle

            colors[node] = 1  # mark as visiting
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            colors[node] = 2  # mark as visited
            return True

        for course in range(numCourses):
            if colors[course] == -1:
                if not dfs(course):
                    return False
        return True
