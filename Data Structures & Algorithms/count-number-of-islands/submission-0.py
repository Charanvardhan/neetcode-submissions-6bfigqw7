class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                queue = [(i,j)]
                if grid[i][j] == "1" and not visited[i][j]:
                    helper(grid, visited, queue, rows, cols)
                    count += 1
        
        return count
                

def helper(grid, visited, queue, rows, cols):

    while len(queue) > 0:
        r, c = queue.pop(0)
        visited[r][c] = True

        if r + 1 < rows and not visited[r+1][c] and grid[r+1][c] == "1":
            queue.append((r+1, c))
        
        if r - 1 > -1 and not visited[r - 1][c] and grid[r - 1][c] == "1":
            queue.append((r-1, c))

        if c + 1< cols and not visited[r][c + 1] and grid[r][c + 1] == "1":
            queue.append((r, c + 1))

        if c - 1 > -1 and not visited[r][c - 1] and grid[r][c - 1] == "1":
            queue.append((r, c - 1))
