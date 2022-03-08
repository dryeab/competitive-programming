class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q, wordList = deque([beginWord]), set(wordList)
        count, visited = 1, set([beginWord])
        
        while q:
            
            for _ in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return count
                
                for i in range(len(word)):
                    for j in range(ord('a'), ord('z')+1):
                        w = word[:i] + chr(j) + word[i+1:]
                        if w in wordList and w not in visited:
                            visited.add(w)
                            q.append(w)
                             
            count += 1
        
        return 0