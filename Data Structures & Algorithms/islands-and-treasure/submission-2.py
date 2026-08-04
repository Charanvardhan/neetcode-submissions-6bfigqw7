from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i,j, 0])
        
        helper(rows, cols, queue, grid)

    

def helper(rows, cols, queue, grid):

    while len(queue) > 0:
        row, col, dist = queue.popleft()

        if row + 1 < rows and grid[row + 1][col] == 2147483647:
            grid[row + 1][col] = dist+1
            queue.append([row + 1, col, dist+1])

        if row - 1 >= 0 and grid[row - 1][col] == 2147483647:
            grid[row - 1][col] = dist+1
            queue.append([row - 1, col, dist+1])
        
        if col + 1 < cols and grid[row][col + 1] == 2147483647:
            grid[row][col + 1] = dist+1
            queue.append([row, col + 1, dist+1])
        
        if col - 1 >= 0 and grid[row][col - 1] == 2147483647:
            grid[row][col - 1] = dist+1
            queue.append([row, col - 1, dist + 1])
