class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        op = 0
        checker = set()

        while right < n:
            if not s[right] in checker:
                checker.add(s[right])
            else:
                while s[right] in checker:
                    checker.remove(s[left])
                    left += 1
                checker.add(s[right])

            right += 1
            op = max(right - left, op)
        
        return op