from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to a set for O(1) lookups
        word_set = set(wordList)
        
        # If the endWord is not in the dictionary, no sequence is possible
        if endWord not in word_set:
            return 0
            
        # Queue for BFS: stores tuples of (current_word, current_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            current_word, length = queue.popleft()
            
            # If we reached the endWord, return the current length
            if current_word == endWord:
                return length
                
            # Generate all possible words that differ by one character
            for i in range(len(current_word)):
                # Try replacing the i-th character with 'a' through 'z'
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    
                    # If the new word is in the dictionary
                    if next_word in word_set:
                        # Mark it as visited by removing it from the set
                        word_set.remove(next_word)
                        queue.append((next_word, length + 1))
                        
        # If the queue is exhausted and we haven't found the endWord
        return 0