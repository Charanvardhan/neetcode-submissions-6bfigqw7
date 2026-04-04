class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            size = len(s)
            encoded += str(size) + "#" + s
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        start = 0
        n = len(s)

        while start < n:
            size = start
            while s[size] != "#":
                size += 1
            print(start, size)
            wordEndIndex = size + 1 + int(s[start:size])

            strs.append(s[size+1: wordEndIndex])

            start = wordEndIndex
        return strs


            

        
