from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        wordSet = set(wordList)
        letters = [chr(i) for i in range(97, 123)]
        L = len(wordList[0])
        
        queue.append([beginWord, 0])
        

        def bfs(queue):

            while queue:
                word, depth = queue.popleft()
                
                if word == endWord:
                    return depth + 1
            
                for i in range(L):
                    for char in letters:
                        newWord = word[:i] + char + word[i+1:]
                        if newWord in wordSet:
                            queue.append([newWord, depth + 1])
                            wordSet.remove(newWord)

            return False
        
        op = bfs(queue)
        if not op:
            return 0
        else:
            return op
                    
        

