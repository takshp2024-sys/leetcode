class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Sort the citations in descending order
        citations.sort(reverse=True)
        
        h_index = 0
        
        # Iterate through the sorted citations
        for i, citation in enumerate(citations):
            # i represents the number of papers we've considered so far (minus 1).
            # The current paper's rank is i + 1.
            # If the current paper has at least (i + 1) citations, then we have at least 
            # (i + 1) papers with at least (i + 1) citations.
            if citation >= i + 1:
                h_index = i + 1
            else:
                # Since the array is sorted descending, all subsequent papers will
                # have fewer citations. We can stop early.
                break
                
        return h_index