from collections import defaultdict

def check(s,t):
    for key,items in t.items():
        if key in s and s[key] >= t[key]:
            continue
        else:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        tcount = defaultdict(int)
        for i in t:
            tcount[i] += 1

        
        l = 0
        r = 0
        scount = defaultdict(int)
        for key,_ in tcount.items():
            scount[key] = 0

        sol = [2**32, 0, 0]

        while r < len(s):
            if not s[r] in tcount:
                r += 1
            else:
                scount[s[r]] += 1
                while check(scount, tcount):
                    if sol[0] > (r-l+1):
                        sol = [(r-l+1), l, r+1]
                    if s[l] in tcount:
                        scount[s[l]] -= 1
                    l += 1
                           
                
                r += 1
        return s[sol[1]:sol[2]]
            
