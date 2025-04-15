# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = {}

        def dfs(node, c):
            if node in color:
                return color[node] == c  

            color[node] = c
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - c):  
                    return False
            return True

        for person in range(1, n + 1):
            if person not in color:
                if not dfs(person, 0):
                    return False
        return True