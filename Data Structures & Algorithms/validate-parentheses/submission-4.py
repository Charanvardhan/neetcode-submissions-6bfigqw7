class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for i in s:
            if i == '(' or i == '{' or i == "[":
                stack.append(i)
                continue
            
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if i == ')' and popped != '(':
                return False
            elif i == '}' and popped != '{':
                return False
            elif i == ']' and popped != '[':
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False


        