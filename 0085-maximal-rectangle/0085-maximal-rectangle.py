class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        for row in matrix:
            # Update the histogram heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
                    
            # Calculate the largest rectangle area in the current histogram
            # using the Monotonic Stack approach (same as LeetCode 84)
            stack = []
            for i in range(cols + 1):
                # Use a dummy height of 0 at the end to flush out the stack
                current_height = heights[i] if i < cols else 0
                
                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                    
                stack.append(i)
                
        return max_area