class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case where n is negative by taking the reciprocal of x
        # and making n positive.
        return x ** n
        
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1.0
        current_product = x
        
        while n > 0:
            # If the current bit in n is 1, multiply the result by the current product
            if n % 2 == 1:
                result *= current_product
                
            # Square the current product for the next bit
            current_product *= current_product
            
            # Shift n to the right by 1 (equivalent to integer division by 2)
            n //= 2
            
        return result