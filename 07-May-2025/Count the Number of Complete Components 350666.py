# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px
            self.size[px] += self.size[py]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edge_count = [0] * n
        
        for u, v in edges:
            uf.union(u, v)
        
        for u, v in edges:
            root = uf.find(u)
            edge_count[root] += 1
        
        components = {}
        for i in range(n):
            root = uf.find(i)
            if root not in components:
                components[root] = []
            components[root].append(i)
        
        complete_count = 0
        for root, nodes in components.items():
            k = len(nodes)
            expected_edges = k * (k - 1) // 2
            actual_edges = edge_count[root]
            if actual_edges == expected_edges:
                complete_count += 1
        
        return complete_count
