from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        l = 0
        r = 0
        
        counter = 0
        tfreq = defaultdict(int)
        sfreq = defaultdict(int)
        window = (2**32,0)

        for i in t:
            tfreq[i] += 1

        need = len(tfreq)

        for r in range(n):
            sfreq[s[r]] += 1
            if s[r] in tfreq and  tfreq[s[r]] == sfreq[s[r]]:
                counter += 1
            
            while l < n and counter == need:
                if window[0] > (r - l + 1):
                    window = (r-l + 1, l)
                sfreq[s[l]] -= 1
                
                if s[l] in tfreq and tfreq[s[l]] > sfreq[s[l]]:
                    print('hi')
                    counter -= 1
                l += 1
        
        print(window, counter)
        return "" if window[0] == 2**32 else s[window[1]: window[0] + window[1]]
                
            
            
            
        