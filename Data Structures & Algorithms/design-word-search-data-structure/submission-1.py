class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        temp = self.trie
        for ch in word:
            if not ch in temp:
                temp[ch] = {}
            temp = temp[ch]
        temp['end'] = True
        
    def search(self, word: str) -> bool:
        return helper(word, self.trie)
        pass
        
def helper(word, trie, startIdx=0):

    for i in range(startIdx, len(word)):
        if word[i] == ".":
            stack = list(trie.keys())
            print(stack)
            for ch in stack:
                if ch == 'end':
                    continue
                if helper(word, trie[ch], i+1):
                    return True
            return False
        else:
            if not trie.get(word[i], False):
                return False
            trie = trie[word[i]]
    
    return trie.get('end', False)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)