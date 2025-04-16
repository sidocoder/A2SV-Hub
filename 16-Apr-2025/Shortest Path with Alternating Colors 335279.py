# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        #create separate red graph and blue graph
        ans = [-1 for _ in range(n)]

        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for i,j in redEdges:
            red_graph[i].append(j)
            
        for a,b in blueEdges:
            blue_graph[a].append(b)
           
        """
        (node,color)
        color == 0 -> red
        color == 1 -> blue
        """
        queue = deque([(0,0),(0,1)])
        visited = set(queue)
        
        dist = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node,color = queue.popleft()
            
                if ans[node] == -1:
                    ans[node] = dist
                else:
                    ans[node] = min(ans[node], dist)
                if color == 0:
                    for child in red_graph[node]:
                        if (child,1) not in visited:
                            visited.add((child,1))
                            queue.append((child,1))
                else:
                    for child in blue_graph[node]:
                        if (child,0) not in visited:
                            visited.add((child,0))
                            queue.append((child,0))

            dist += 1
            
        return ans
            



        
