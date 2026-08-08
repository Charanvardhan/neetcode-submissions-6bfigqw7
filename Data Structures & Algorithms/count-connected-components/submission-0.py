from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for i,j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        def bfs(node, visited):
            visited.add(node)

            for neighbour in adjList[node]:
                if not neighbour in visited:
                    bfs(neighbour, visited)

        visited = set()     
        op = 0
        for i in range(n):
            if i not in visited:
                op += 1
                bfs(i, visited)
        
        return op
        