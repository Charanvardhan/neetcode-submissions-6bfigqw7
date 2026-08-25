class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if i.isalnum():
                t += i
        print(t)
        s = t.lower()
        size = len(s)
        if size % 2 == 0:
            l = (size//2) - 1
            r = size//2
        
        else:
            l = r = (size//2)

        while l>=0 and r < size:

            if s[l] != s[r]:
                return False
            l -= 1
            r += 1
        
        return True
        