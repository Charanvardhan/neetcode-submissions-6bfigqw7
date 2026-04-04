class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            if i == '+' or i == "-" or i == "*":
                k = eval(stack[-2] + i + stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(k))
            elif i == "/":
                k = eval(stack[-2] + i  + stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(k)))
                print(stack)
            else:
                stack.append(i)
        
        return int(stack[-1])
