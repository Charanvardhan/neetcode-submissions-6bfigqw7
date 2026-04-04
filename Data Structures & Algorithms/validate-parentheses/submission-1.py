class Solution:
    def isValid(self, s: str) -> bool:
        validator = []
        for i in s:
            if len(validator) == 0:
                validator.append(i)
                continue
            if i == ')' and validator[-1] != "(":
                return False
            elif i == ']' and validator[-1] != "[":
                return False
            elif i == "}" and validator[-1] != "{":
                return False
            
            
            if i == ')' or i == ']' or i =='}':
                validator.pop()
            else:
                validator.append(i)

        return True if len(validator) == 0 else False