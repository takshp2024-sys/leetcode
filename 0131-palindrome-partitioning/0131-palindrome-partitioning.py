class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
            
        def backtrack(start: int, current_partition: List[str]):
            # Base case: If we've reached the end of the string, we have a valid partition
            if start == len(s):
                result.append(list(current_partition))
                return
                
            # Try every possible substring starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is a palindrome, include it and recurse
                if is_palindrome(substring):
                    current_partition.append(substring)
                    backtrack(end, current_partition)
                    current_partition.pop()
                    
        backtrack(0, [])
        return result