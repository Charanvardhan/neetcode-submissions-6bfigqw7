class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                queue = [(i,j)]
                if grid[i][j] == 1 and not visited[i][j]:
                    maxArea = max(maxArea, helper(grid, visited, queue, rows, cols, 0))
                           
        return maxArea
                

def helper(grid, visited, queue, rows, cols, area):

    while len(queue) > 0:
        r, c = queue.pop(0)
        if visited[r][c]:
            continue
        area += 1
        visited[r][c] = True

        if r + 1 < rows and not visited[r+1][c] and grid[r+1][c] == 1:
            queue.append((r+1, c))
        
        if r - 1 > -1 and not visited[r - 1][c] and grid[r - 1][c] == 1:
            queue.append((r-1, c))

        if c + 1< cols and not visited[r][c + 1] and grid[r][c + 1] == 1:
            queue.append((r, c + 1))

        if c - 1 > -1 and not visited[r][c - 1] and grid[r][c - 1] == 1:
            queue.append((r, c - 1))

    return area
        