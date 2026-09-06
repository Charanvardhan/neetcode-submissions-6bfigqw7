class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        op = 0
        left = 0
        right = n - 1

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            op = max(op, area)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return op