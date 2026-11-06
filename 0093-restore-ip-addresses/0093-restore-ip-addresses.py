class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start: int, parts: List[str]):
            # Base case: If we have 4 parts and used all characters, it's a valid IP
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
                
            # If we still need parts, but we've run out of string, stop
            if start == len(s):
                return
                
            # Try taking 1, 2, or 3 digits for the current part
            for length in range(1, 4):
                # Don't go out of bounds
                if start + length > len(s):
                    break
                    
                part = s[start : start + length]
                
                # Check for leading zeros (e.g., "01" is invalid, but "0" is valid)
                if len(part) > 1 and part[0] == '0':
                    continue
                    
                # Check if the part is within the valid range (0 to 255)
                if int(part) <= 255:
                    parts.append(part)
                    backtrack(start + length, parts)
                    parts.pop() # Backtrack
                    
        backtrack(0, [])
        return result