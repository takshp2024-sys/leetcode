class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            # Decrement columnNumber by 1 to make it 0-indexed
            # This maps 1-26 to 0-25, corresponding to 'A'-'Z'
            columnNumber -= 1
            
            # Find the current character
            remainder = columnNumber % 26
            result.append(chr(remainder + ord('A')))
            
            # Move to the next "digit"
            columnNumber //= 26
            
        # The characters were found from right to left, so reverse them
        return "".join(reversed(result))