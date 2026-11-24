class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
            
        # Define the word mappings
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n: int) -> str:
            # Converts a number < 1000 to words
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)
                
        result = ""
        for i in range(4): # 4 chunks for up to 2^31 - 1 (Billions)
            # Extract the last 3 digits
            chunk = num % 1000
            if chunk != 0:
                # Convert the chunk to words and append the scale (Thousand, Million, etc.)
                chunk_words = helper(chunk)
                result = chunk_words + thousands[i] + " " + result
            # Move to the next chunk
            num //= 1000
            
        # Remove trailing spaces
        return result.strip()