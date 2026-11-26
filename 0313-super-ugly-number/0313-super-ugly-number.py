class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp[i] will store the (i+1)-th super ugly number
        dp = [0] * n
        dp[0] = 1  # The first super ugly number is 1
        
        # Pointers for each prime, initially at index 0
        pointers = [0] * len(primes)
        
        for i in range(1, n):
            # Calculate the next potential super ugly number for each prime
            next_candidates = [dp[pointers[j]] * primes[j] for j in range(len(primes))]
            
            # The next super ugly number is the minimum of these candidates
            next_ugly = min(next_candidates)
            dp[i] = next_ugly
            
            # Advance the pointer(s) that produced the minimum value
            for j in range(len(primes)):
                if next_candidates[j] == next_ugly:
                    pointers[j] += 1
                    
        return dp[n - 1]