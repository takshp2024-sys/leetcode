from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        # If the total length of all words is greater than the string, it's impossible
        if len(s) < total_len:
            return []
        
        # Count the frequency of each word in 'words'
        word_count = Counter(words)
        result = []
        
        # We only need to perform the sliding window starting from the first 'word_len' positions.
        # Any starting position beyond that can be covered by shifting the window by 'word_len'.
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            # Slide the window across the string in steps of 'word_len'
            while right + word_len <= len(s):
                # Extract the word at the right pointer
                word = s[right:right + word_len]
                right += word_len
                
                # If the word is part of our target words
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    # If we have too many of this word, shrink the window from the left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                        
                    # If the window contains exactly all the words, record the start index
                    if count == num_words:
                        result.append(left)
                        # Shrink the window from the left to look for the next valid substring
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # If the word is not in our target words, the current window is invalid.
                    # Reset the window and start from the next position.
                    current_count.clear()
                    count = 0
                    left = right
                    
        return result