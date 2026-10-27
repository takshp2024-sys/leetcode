class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base case: If the string length is 2 * n, we have used all parentheses
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: We can add an opening parenthesis if we haven't used all 'n' of them
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: We can add a closing parenthesis only if there are unmatched opening parentheses
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the backtracking with an empty string, 0 open, and 0 close
        backtrack("", 0, 0)
        
        return result