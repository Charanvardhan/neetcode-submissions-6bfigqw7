class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for st in strs:
            count = [0 for j in range(26)]
            for i in st:
                pos = (ord(i)-97)
                count[pos] += 1
            
            count = tuple(count)
            print(hashmap)
            if not hashmap.get(count):
                hashmap[count] = [st]
            else:
                if hashmap.get(count):
                    hashmap[count].append(st)

        return hashmap.values()
            

        