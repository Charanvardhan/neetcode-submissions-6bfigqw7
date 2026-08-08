from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        def dfs(node, visited):
            visited.add(node)
            for neighbour in adjList[node]:
                if not neighbour in visited:
                    dfs(neighbour, visited)
        
        visited = set()
        dfs(0, visited)
        if len(visited) != n:
            return False
        
        if len(edges) != n-1:
            return False

        return True

            
        