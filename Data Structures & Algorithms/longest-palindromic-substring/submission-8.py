class Solution:
    def longestPalindrome(self, s: str) -> str:
        rows = cols = len(s)
        matrix = [[False for i in range(cols)] for i in range(rows)]
        maxSize = 0
        start = -1

        for i in range(rows-1, -1, -1):
            for j in range(i, cols):
                if i == j:
                    matrix[i][j] = True
                elif i+1 == j and s[i] == s[j]:       
                    matrix[i][j] = True          
                else: 

                    matrix[i][j] = (s[i] == s[j]) and matrix[i+1][j-1]

                if matrix[i][j] and maxSize < j - i + 1:
                    maxSize = j - i + 1
                    start = i
        
        return s[start: start+maxSize]
        