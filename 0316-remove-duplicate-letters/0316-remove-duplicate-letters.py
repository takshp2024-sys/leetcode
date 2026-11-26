class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count the frequency of each character
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        stack = []
        in_stack = set()
        
        for char in s:
            # Decrement the remaining count of the current character
            count[char] -= 1
            
            # If the character is already in the stack, skip it
            if char in in_stack:
                continue
                
            # Maintain the monotonic increasing property
            # Pop if the top of the stack is greater than the current char
            # AND the top char appears later in the string
            while stack and stack[-1] > char and count[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
                
            # Add the current character to the stack and mark as seen
            stack.append(char)
            in_stack.add(char)
            
        return "".join(stack)