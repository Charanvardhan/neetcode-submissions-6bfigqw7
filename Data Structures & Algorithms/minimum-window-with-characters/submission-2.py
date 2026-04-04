class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        tcount = dict()
        scount = dict()

        for i in t:
            if i in tcount:
                tcount[i] += 1
            else:
                tcount[i] = 1
            
            if i not in scount:
                scount[i] = 0
            
        l, r = 0, 0
        totalChr = len(tcount)
        currentChr = 0
        sol = [2**32, 0, 0]
        print(totalChr, tcount, scount)

        while r < len(s):
            if s[r] in scount:
                scount[s[r]] += 1
                if tcount[s[r]] == scount[s[r]]:
                    currentChr += 1
                
                while currentChr == totalChr:
                    if sol[0] > (r-l +1):
                        sol = [(r-l) +1, l, r]
                    if s[l] in scount:
                        scount[s[l]] -= 1
                        if tcount[s[l]] > scount[s[l]]:
                            currentChr -= 1
                    l += 1

            r+=1

        # if currentChr == totalChr:
        #     if sol[0] > (r-l +1):
        #         sol = [(r-l) +1, l, r]

        if sol[0] == 2**32:
            return ""

        print(sol)
        return s[sol[1]:sol[2]+1]
                    
        