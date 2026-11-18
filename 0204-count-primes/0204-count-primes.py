class Solution:
    def countPrimes(self, n: int) -> int:
        # If n is 0 or 1, there are no prime numbers less than n
        if n <= 2:
            return 0
            
        # Initialize a boolean array to mark primes (True means prime)
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Iterate up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as not prime
                # Start from i*i to avoid redundant marking
                for j in range(i * i, n, i):
                    is_prime[j] = False
                    
        # Count the number of True values in the array
        return sum(is_prime)