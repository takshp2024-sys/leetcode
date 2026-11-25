class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the string s into words
        words = s.split()
        
        # If the number of characters in pattern and words in s don't match, return False
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check mapping from character to word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Check mapping from word to character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True