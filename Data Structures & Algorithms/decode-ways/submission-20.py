class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == 0:
            return 0
        
        mem = {}
        
        def traversal(i):
            nonlocal mem

            if i in mem:
                return mem[i]
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            
            
            temp = traversal(i+1)
            if i+1 < n and 9 < int(s[i] + s[i+1]) < 27:
                temp += traversal(i + 2)
            
            mem[i] = temp
            return temp
        

        return traversal(0)
