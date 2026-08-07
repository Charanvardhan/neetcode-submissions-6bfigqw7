from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for val, key in prerequisites:
            adjList[key].append(val)
        
        mem = [0 for i in range(numCourses)]

        def dfs(node):
            if mem[node] == 1:
                return False
            if mem[node] == 2:
                return True

            mem[node] = 1
            for neighbour in adjList[node]:
                if not dfs(neighbour):
                    return False
            mem[node] = 2

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

            
