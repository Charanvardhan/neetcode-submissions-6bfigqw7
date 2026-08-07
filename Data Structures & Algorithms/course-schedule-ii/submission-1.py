from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for key, val in prerequisites:
            adjList[key].append(val)
        
        mem = [0] * numCourses
        op = []

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
            op.append(node)
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []
            # else:
            #     op.append(course)

        return op