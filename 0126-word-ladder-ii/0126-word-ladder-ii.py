from collections import defaultdict, deque
import string

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # If endWord is not in the dictionary, no sequence exists
        if endWord not in wordList:
            return []
            
        # Dictionary to hold the predecessors of each word in the shortest path graph
        parents = defaultdict(list)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        
        # BFS level by level
        current_level = {beginWord}
        visited = set()
        found = False
        
        while current_level and not found:
            # Add the current level to visited so we don't revisit them in future levels
            visited.update(current_level)
            next_level = set()
            
            for word in current_level:
                # Try changing every character to 'a'-'z'
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                            
                        next_word = word[:i] + c + word[i+1:]
                        
                        # If the new word is valid and not visited yet
                        if next_word in wordSet and next_word not in visited:
                            # If we reached the endWord, we found a shortest path
                            if next_word == endWord:
                                found = True
                                
                            # Record the parent relationship (word -> next_word)
                            parents[next_word].append(word)
                            next_level.add(next_word)
                            
            current_level = next_level
            
        # DFS Backtracking to build all paths
        result = []
        def dfs(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()
                
        # If a path was found, reconstruct it starting from the endWord
        if found:
            dfs(endWord, [endWord])
            
        return result