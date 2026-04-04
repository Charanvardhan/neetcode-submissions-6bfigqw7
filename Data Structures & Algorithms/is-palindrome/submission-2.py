class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join([char for char in s if char.isalnum()])
        string = string.lower()
        
        print(string)
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True

    
        