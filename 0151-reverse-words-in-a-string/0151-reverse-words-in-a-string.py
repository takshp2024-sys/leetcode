class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() automatically removes leading/trailing spaces and splits by multiple spaces
        words = s.split()
        
        # Reverse the list of words
        words.reverse()
        
        # Join them back with a single space
        return " ".join(words)