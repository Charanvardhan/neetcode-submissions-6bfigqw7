class Solution:
    def numDecodings(self, s: str) -> int:
        decoder = {"1": 'A', "2":"B", "3":"C", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J", "10":"K", "11":"L", "12":"M", "13":"N", "14":"O",          "15":"P", "16":"Q", "17":"R", "18":"S", "19":"T", "20":"U", "21":"V", "22":"W", "23":"X", "24":"Y", "25":"Z", "26":"D"}

        n = len(s)
        mem = {}
        def traversal(i):
            if i in mem:
                return mem[i]
            if i == n:
                return 1
            
            if i > n:
                return 0

            if not s[i] in decoder:
                return 0
            
            total = traversal(i+1)
            if i+ 1 < n and (s[i] + s[i+1]) in decoder:
                total += traversal(i + 2)
            mem[i] = total
            return total

        return traversal(0)
            
            

            

        