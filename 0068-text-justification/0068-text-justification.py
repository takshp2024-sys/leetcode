class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding the new word exceeds maxWidth
            # The length includes the word itself and at least one space if it's not the first word
            if current_length + len(word) + len(current_line) > maxWidth:
                # Format the current line
                if len(current_line) == 1:
                    # Edge case: only one word in the line
                    result.append(current_line[0] + " " * (maxWidth - current_length))
                else:
                    # Calculate spaces needed
                    total_spaces = maxWidth - current_length
                    gaps = len(current_line) - 1
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    
                    line_str = ""
                    for i in range(gaps):
                        line_str += current_line[i]
                        # Add spaces: the first 'extra_spaces' gaps get one extra space
                        spaces_to_add = space_per_gap + (1 if i < extra_spaces else 0)
                        line_str += " " * spaces_to_add
                    line_str += current_line[-1] # Add the last word
                    result.append(line_str)
                
                # Reset for the next line
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
                
        # Handle the last line: left-justified with a single space between words
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result