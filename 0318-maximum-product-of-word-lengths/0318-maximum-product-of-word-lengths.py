class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Create a list to store the bitmask for each word
        masks = []
        for word in words:
            mask = 0
            for char in word:
                # Set the bit corresponding to the character
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)
            
        max_product = 0
        n = len(words)
        
        # Compare every pair of words
        for i in range(n):
            for j in range(i + 1, n):
                # If the bitwise AND is 0, they share no common letters
                if (masks[i] & masks[j]) == 0:
                    max_product = max(max_product, len(words[i]) * len(words[j]))
                    
        return max_product