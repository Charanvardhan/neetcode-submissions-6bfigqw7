class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        bestl, bestr = 0,1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right

        for i in range(n-1):
            oleft, oright = expand(i,i)
            if bestr - bestl < oright - oleft:
                bestr, bestl = oright, oleft

            eleft, eright = expand(i,i+1)
            if bestr - bestl < eright - eleft:
                bestr, bestl = eright, eleft
        print(bestl, bestr)
        return s[bestl:bestr]

            