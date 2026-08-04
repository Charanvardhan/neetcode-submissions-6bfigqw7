from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshfruits = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshfruits += 1
                elif grid[i][j] == 2:
                    queue.append([i, j, 0])
                
        return helper(grid, queue, rows, cols, freshfruits)
    

def helper(grid, queue, rows, cols, freshfruits):
    minutes = 0
    
    while len(queue) > 0:
        row, col, minute = queue.popleft()

        minutes = max(minute, minutes)

        if row + 1 < rows and grid[row + 1][col] == 1:
            grid[row + 1][col] = 2
            freshfruits -= 1
            queue.append([row + 1, col, minute + 1])

        
        if col + 1 < cols and grid[row][col + 1] == 1:
            grid[row][col + 1] = 2
            freshfruits -= 1
            queue.append([row, col + 1, minute + 1])
        
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            grid[row - 1][col] = 2
            freshfruits -= 1
            queue.append([row - 1, col, minute + 1])

        if col - 1 >= 0  and grid[row][col - 1] == 1:
            grid[row][col - 1] = 2
            freshfruits -= 1
            queue.append([row, col - 1, minute + 1])
        
    if freshfruits == 0:
        return minutes
    else:
        return -1