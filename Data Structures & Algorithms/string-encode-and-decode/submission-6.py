class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append("#")
            encoded.append(word)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+= 1
            
            
            wordLength = int(s[i:j])
            decoded.append(s[j+1:j+1+wordLength])
            i = wordLength + j + 1
        
        return decoded

