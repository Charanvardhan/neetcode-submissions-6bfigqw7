class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in range(len(tokens)):
            temp = tokens[i]
            if tokens[i] == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = str(a + b)
                
            elif tokens[i] == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = str(a - b)
            elif tokens[i] == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = str(a * b)
            elif tokens[i] == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                temp = str(int(a / b))
                
            
            stack.append(temp)
            
        return int(stack.pop())