class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        
        # Iterate through the string in steps of 2
        for i in range(0, len(s), 2):
            # If the pair of characters is different, we need 1 change
            if s[i] != s[i+1]:
                changes += 1
                
        return changes