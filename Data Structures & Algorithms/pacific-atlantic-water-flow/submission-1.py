from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        pacific_q = deque()
        atlantic_q = deque()

        for c in range(cols):
            pacific_q.append((0, c))
            pacific[0][c] = True
            atlantic_q.append((rows - 1, c))
            atlantic[rows - 1][c] = True

        for r in range(rows):
            pacific_q.append((r, 0))
            pacific[r][0] = True
            atlantic_q.append((r, cols - 1))
            atlantic[r][cols - 1] = True

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and not visited[nr][nc]
                            and heights[nr][nc] >= heights[row][col]):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

        bfs(pacific_q, pacific)
        bfs(atlantic_q, atlantic)

        return [[r, c] for r in range(rows) for c in range(cols) if pacific[r][c] and atlantic[r][c]]