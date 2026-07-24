class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in range(len(tokens)):
            
            if tokens[i] == "+" or tokens[i] == "-" or tokens[i] == "*":
                b = stack.pop()
                a = stack.pop()
                temp = str(eval(a+tokens[i]+ b))
                stack.append(temp)
            elif tokens[i] == "/":
                b = stack.pop()
                a = stack.pop()
                temp = str(int(eval(a+tokens[i]+ b)))
                stack.append(temp)
            
            else:
                stack.append(tokens[i])
            
        return int(stack.pop())