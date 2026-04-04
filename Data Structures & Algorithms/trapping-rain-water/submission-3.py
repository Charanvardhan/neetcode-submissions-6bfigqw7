class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0 for i in range(n)]
        maxR = [0 for i in range(n)]
        minLR = [0 for i in range(n)]

        tempMax = 0
        for i in range(n-1):
            tempMax = max(tempMax, height[i])
            maxL[i+1] = tempMax
        
        tempMax = 0
        for j in range(n-1, 0, -1):
            tempMax = max(tempMax, height[j])
            maxR[j-1] = tempMax

        sol = 0
        
        for i in range(n):
            expected = min(maxL[i], maxR[i]) - height[i]
            if expected > 0:
                sol += expected

        return sol 
        
        

