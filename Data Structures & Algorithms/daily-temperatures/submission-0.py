class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        stack.append((temperatures[0],0))
        n = len(temperatures)
        results = [0] * n

        for i in range(1, n):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                results[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        
        return results
