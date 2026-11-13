class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        
        for char in columnTitle:
            # Convert the character to its 1-26 value
            # ord('A') is 65, so ord(char) - ord('A') + 1 gives A=1, B=2, ..., Z=26
            value = ord(char) - ord('A') + 1
            
            # Shift the current result by one base-26 digit and add the new value
            result = result * 26 + value
            
        return result