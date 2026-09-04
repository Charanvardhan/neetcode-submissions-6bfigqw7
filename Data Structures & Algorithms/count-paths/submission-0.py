class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            matrix[i][n-1] = 1
        
        for j in range(n):
            matrix[m-1][j] = 1
        
        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                matrix[row][col] = matrix[row+1][col] + matrix[row][col+1]
        
        return matrix[0][0]
        

        