class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""
        lc = 0
        rc = 0

        def dfs(cur, lc, rc):
            if lc == n:
                while rc < lc:
                    cur += ')'
                    rc += 1
                res.append(cur)
                return
            
            dfs(cur + "(", lc + 1, rc)

            if lc > rc:
                dfs(cur + ")", lc, rc + 1)
            
        dfs(cur, lc, rc)

        return res