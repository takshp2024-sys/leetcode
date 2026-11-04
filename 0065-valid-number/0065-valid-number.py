class Solution:
    def isNumber(self, s: str) -> bool:
        # Flags to track what we've seen
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # A sign is only valid if it's the first character 
                # OR it immediately follows an exponent ('e' or 'E')
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char in "eE":
                # An exponent is only valid if we've seen a digit 
                # and we haven't seen an exponent yet
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because we need at least one digit after the exponent
                seen_digit = False
            elif char == ".":
                # A dot is only valid if we haven't seen a dot or an exponent yet
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                # Any other character is invalid
                return False
                
        # The string is valid only if we ended with at least one digit 
        # (this catches cases like "1e" or "-" or ".")
        return seen_digit