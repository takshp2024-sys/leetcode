class Solution:
    def countAndSay(self, n: int) -> str:
        # The base case
        current_string = "1"
        
        # We need to generate the sequence n - 1 times
        for _ in range(n - 1):
            next_string = []
            count = 1
            
            # Iterate through the current string to generate the next one
            for i in range(1, len(current_string)):
                if current_string[i] == current_string[i - 1]:
                    # If the current character is the same as the previous, increment the count
                    count += 1
                else:
                    # If it's different, append the count and the previous character
                    next_string.append(str(count))
                    next_string.append(current_string[i - 1])
                    # Reset count for the new character
                    count = 1
                    
            # Don't forget the last group of characters
            next_string.append(str(count))
            next_string.append(current_string[-1])
            
            # Join the list into a string for the next iteration
            current_string = "".join(next_string)
            
        return current_string