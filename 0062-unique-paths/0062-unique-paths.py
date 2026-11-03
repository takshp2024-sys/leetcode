import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to take (m - 1) down steps and (n - 1) right steps.
        # The total number of steps is (m + n - 2).
        # We calculate the combinations formula: nCr = n! / (r! * (n-r)!)
        
        total_steps = m + n - 2
        down_steps = m - 1
        
        # Python's math.comb calculates combinations optimally without overflow
        return math.comb(total_steps, down_steps)