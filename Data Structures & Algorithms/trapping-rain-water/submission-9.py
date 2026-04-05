class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0


        leftMax = height[0]
        rightMax = height[n-1]
        left = 0
        right = n-1
        sol = 0

        while left < right:
            if leftMax <= rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                sol += leftMax - height[left]
                
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                sol += rightMax - height[right]
                
            
        return sol
                
