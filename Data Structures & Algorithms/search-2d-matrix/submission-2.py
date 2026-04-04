class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        # Phase 1: Find the candidate row
        while top <= bottom:                        # ✅ <= not 
            mid = (top + bottom) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1

        if top == rows:
            row = bottom
        elif bottom == -1 or matrix[bottom][-1] < target:   # ← runs regardless
            row = top

        # Phase 2: Binary search within that row
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
