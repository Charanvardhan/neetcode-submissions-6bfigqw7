class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = height[0]
        rMax = height[-1]
        n = len(height)

        l = 1
        r = n - 2
        sol = 0

        while l <= r:
            if lMax > rMax:
                temp = rMax - height[r]
                if temp > 0:
                    sol += temp
                rMax = max(height[r], rMax)
                r -= 1
            else:
                temp = lMax - height[l]
                if temp > 0:
                    sol += temp
                lMax = max(lMax, height[l])
                l+= 1
        
        return sol
                    

        