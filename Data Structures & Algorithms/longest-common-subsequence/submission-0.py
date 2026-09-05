class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        grid = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        print(rows, cols, grid)
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if text1[row-1] == text2[col-1]:
                    grid[row][col] = grid[row -1][col-1] + 1
                
                else:
                    print(row, col)
                    grid[row][col] = max(grid[row-1][col],  grid[row][col-1])
                
        return grid[rows][cols]

        
        