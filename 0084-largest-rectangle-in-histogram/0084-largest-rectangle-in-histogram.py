class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We append a 0 to the end to ensure all remaining bars in the stack are processed
        heights.append(0)
        stack = [] # Stack will store indices
        max_area = 0
        
        for i, h in enumerate(heights):
            # While the current bar is shorter than the bar at the top of the stack
            while stack and heights[stack[-1]] > h:
                # Pop the height of the bar
                height = heights[stack.pop()]
                # Calculate the width
                # If the stack is empty, it means the popped bar was the smallest so far,
                # so the width extends all the way to the left (index 0).
                # Otherwise, the width extends from the current index i back to the index 
                # after the new top of the stack.
                width = i if not stack else i - stack[-1] - 1
                
                # Update max_area
                max_area = max(max_area, height * width)
                
            # Push the current index onto the stack
            stack.append(i)
            
        return max_area