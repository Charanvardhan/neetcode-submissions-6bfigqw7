from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        queue = deque()

        for r in range(rows):
            if board[r][0] == 'O':
                queue.append((r,0))
                board[r][0] = 'Z'   
            if board[r][cols - 1] == 'O':
                queue.append((r,cols - 1))
                board[r][cols - 1] = 'Z' 

        for c in range(cols):
            if board[0][c] == 'O':
                queue.append((0,c))    
                board[0][c] = 'Z'  
            
            if board[rows - 1][c] == 'O':
                queue.append((rows - 1,c))    
                board[rows - 1][c] = 'Z' 
        
        def bfs(queue):
            while queue:
                row, col = queue.popleft()

                for dr, dc in ((0,1), (1,0), (0, -1), (-1, 0)):
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                        board[nr][nc] = 'Z'
                        queue.append((nr, nc))
        
        bfs(queue)
    
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z':
                    board[i][j] = 'O'