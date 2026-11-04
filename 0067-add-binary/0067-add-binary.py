class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers starting from the end of both strings
        i, j = len(a) - 1, len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            # Add digit from string a if available
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            # Add digit from string b if available
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current bit is the remainder of the sum divided by 2
            result.append(str(total % 2))
            # The carry is the integer division of the sum by 2
            carry = total // 2
            
        # Since we built the result from right to left, we need to reverse it
        return "".join(reversed(result))