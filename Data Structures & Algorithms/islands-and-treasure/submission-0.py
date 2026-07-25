class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    self.dfs(grid, i, j, 0, rows, cols)

    def dfs(self, grid, r, c, distance, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] == -1:
            return
        if grid[r][c] < distance:
            return  # a shorter (or equal) path already recorded here

        grid[r][c] = distance

        self.dfs(grid, r + 1, c, distance + 1, rows, cols)
        self.dfs(grid, r - 1, c, distance + 1, rows, cols)
        self.dfs(grid, r, c + 1, distance + 1, rows, cols)
        self.dfs(grid, r, c - 1, distance + 1, rows, cols)