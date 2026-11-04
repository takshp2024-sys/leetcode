class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by '/' to get the individual components
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.':
                # Ignore empty strings (from multiple slashes) and current directory
                continue
            elif part == '..':
                # Go up one directory level if possible
                if stack:
                    stack.pop()
            else:
                # It's a valid directory or file name
                stack.append(part)
                
        # Join the stack elements with '/' and prepend a leading '/'
        return '/' + '/'.join(stack)