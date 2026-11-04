class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
            
        # We only need to keep track of the previous two steps
        prev2 = 1  # ways to reach step 1
        prev1 = 2  # ways to reach step 2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return prev1