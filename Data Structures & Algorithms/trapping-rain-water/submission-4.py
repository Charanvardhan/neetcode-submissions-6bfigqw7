class Solution:
    def trap(self, height: List[int]) -> int:
        l = 1
        r = len(height) - 2
        maxL = height[0]
        maxR = height[-1]
        sol = 0

        while l <= r:
            print(l,r, sol, maxL, maxR)
            if maxL > maxR:
                canContain = maxR - height[r]
                if canContain > 0:
                    sol += canContain
                maxR = max(height[r], maxR)
                r -= 1
            else:
                canContain = maxL - height[l]
                maxL = max(height[l], maxL)
                l += 1
                if canContain > 0:
                    sol += canContain
            print(l,r, sol, maxL, maxR, " end")

        return sol        

        