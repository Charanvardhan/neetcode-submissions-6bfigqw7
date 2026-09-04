class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for word in strs:
            n = len(word)
            string += str(n) + '#' + word
        
        return string


# 5#hello10#worldworld
    def decode(self, s: str) -> List[str]:
        op = []
        ind = 0
        print(s)
        while ind < len(s):
            diff = ind
            while s[diff + 1] != '#':
                diff += 1
            size = int(s[ind:diff+1])
            word = s[diff+2: diff+2+size]
            op.append(word)
            ind = diff+2+size
        return op