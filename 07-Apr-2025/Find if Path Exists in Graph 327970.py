# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:          
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node,visited):
            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    found = dfs(neighbour,visited)
                    if found:
                        return True
            return False
        graph = defaultdict(list)

        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        return dfs(source,visited)
    