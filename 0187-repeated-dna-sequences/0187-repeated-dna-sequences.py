class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        
        # Iterate through the string, extracting 10-letter substrings
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)
                
        return list(repeated)