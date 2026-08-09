class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1 for i in range(n + 1)]

        def find(x):
            while parents[x] != x:
                x = find(parents[x])
            return parents[x]
        
        def union(u, v):
            root_u, root_v = find(u), find(v)

            if root_u == root_v:
                return False
            
            if rank[root_u] < rank[root_v]:
                root_u, root_v = root_v, root_u

            parents[root_v] = root_u
            rank[root_u] += rank[root_v]
            return True
        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
            
        return []
        

        
        