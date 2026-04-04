class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        sol = 0
        n = len(s)
        back = 0
        front = 0
        charHolder = {}

        while front < n:
            if s[front] in charHolder and charHolder[s[front]] >= back:
                back = charHolder[s[front]] + 1

            charHolder[s[front]] = front
            sol = max(sol, front - back + 1)
            front += 1

        return sol