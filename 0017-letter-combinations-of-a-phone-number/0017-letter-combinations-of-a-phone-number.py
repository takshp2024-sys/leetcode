class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, there are no combinations
        if not digits:
            return []
        
        # Mapping of digits to their corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_path: str):
            # Base case: If the current path length equals the number of digits,
            # we have formed a complete combination.
            if len(current_path) == len(digits):
                result.append(current_path)
                return
            
            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]
            
            # Iterate through each letter and explore further
            for letter in letters:
                # Append the letter and move to the next digit
                backtrack(index + 1, current_path + letter)
                
        # Start the backtracking process from index 0 with an empty path
        backtrack(0, "")
        
        return result