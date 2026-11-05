class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def solve(a: str, b: str) -> bool:
            # If the substring pair is already computed, return the cached result
            if (a, b) in memo:
                return memo[(a, b)]
                
            # Base case: if the strings are identical, they are scrambled
            if a == b:
                return True
                
            # Base case: if lengths differ or character frequencies don't match, return False
            if len(a) != len(b) or sorted(a) != sorted(b):
                return False
                
            n = len(a)
            
            # Try all possible split points from 1 to n-1
            for i in range(1, n):
                # Case 1: No swap - match a's left with b's left, and a's right with b's right
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                    
                # Case 2: Swap - match a's left with b's right, and a's right with b's left
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
                    
            # If no split works, the strings are not scrambled
            memo[(a, b)] = False
            return False
            
        return solve(s1, s2)