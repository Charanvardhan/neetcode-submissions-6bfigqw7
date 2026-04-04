class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        maxArea = 0
        stack = list()
        stack.append((l, heights[0]))
        l+=1


        while l < n:
            if heights[l] == stack[-1][1]:
                l+=1

            elif heights[l] > stack[-1][1]:
                stack.append((l, heights[l]))
                l+=1
            
            else:
                start = l
                while len(stack) > 0 and stack[-1][1] > heights[l]:
                    area = (l - stack[-1][0]) * stack[-1][1]
                    print(area)
                    maxArea = max(area, maxArea)
                    start, _ = stack.pop()
                
                stack.append((start, heights[l]))
                l+=1
            

        while len(stack) > 0:
            area = (l - stack[-1][0]) * stack[-1][1]
            print(area, l, stack[-1][0])
            maxArea = max(area, maxArea)
            stack.pop()
        
        return maxArea

        
        