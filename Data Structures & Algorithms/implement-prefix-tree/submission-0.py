class PrefixTree:

    def __init__(self): 
        self.trie = {'end':False}
        
        

    def insert(self, word: str) -> None:
        temp = self.trie
        for ch in word:
            if ch not in temp:

                temp[ch] = {'end':False}
            # print(self.trie)
            temp = temp[ch]
        
        temp['end'] = True
          

    def search(self, word: str) -> bool:
        temp = self.trie

        for ch in word: 
            if ch in temp:
                temp = temp[ch]
                continue
            return False
        return temp['end']
        pass

    def startsWith(self, prefix: str) -> bool:
        temp = self.trie
        for ch in prefix:
            if ch in temp:
                temp = temp[ch]
                continue
            return False
        return True
        pass


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)