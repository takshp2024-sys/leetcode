class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge case where either number is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # The maximum length of the product of an m-digit and n-digit number is m + n
        res = [0] * (m + n)
        
        # Iterate through the digits in reverse order (from least significant to most)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Convert characters to integers by calculating their ASCII difference
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # Multiply the two digits
                mul = digit1 * digit2
                
                # Determine the positions in the result array
                # p2 is the current position, p1 is the carry position
                p2 = i + j + 1
                p1 = i + j
                
                # Add the multiplication result to the current position
                total = mul + res[p2]
                
                # Update the current position with the single digit (modulo 10)
                res[p2] = total % 10
                # Add the carry to the next position
                res[p1] += total // 10
                
        # Convert the array of integers back to a string, skipping any leading zeros
        # Find the first non-zero digit
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        # Join the remaining digits
        return "".join(str(x) for x in res[start:])