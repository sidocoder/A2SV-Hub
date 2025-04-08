# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in trust:
            graph[a].append(b)

        for i in range(1, n + 1):           
            if len(graph[i]) == 0 and sum(i in value for value in graph.values()) == n - 1:
                return i
        
        return -1
