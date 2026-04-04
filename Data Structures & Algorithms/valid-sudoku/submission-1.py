class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in range(9):
            checker = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in checker:
                        return False
                    checker.add(board[row][col])
                
        
        for col in range(9):
            checker = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in checker:
                        return False
                    checker.add(board[row][col])

        print('hi')

        for row in range(0,9,3):
            rowmax = row + 3
            
            for col in range(0,9,3):
                colmax = col + 3
                checker = set()
                for i in range(row, rowmax):
                    for j in range(col, colmax):
                        if board[i][j] != ".":
                            if board[i][j] in checker:
                                return False
                            checker.add(board[i][j])

        
        return True


        