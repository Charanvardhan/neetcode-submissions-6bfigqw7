class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        
        count = 0

        for i in range(n):
            count += palindrome(s, i, i, n)
            
        
        for i in range(n-1):
            count += palindrome(s, i, i+1, n)

        return count 


def palindrome(s, l, r, n):
    count = 0
    while l > -1 and r < n:
        if s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        else:
            break
        
    return count


        