class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the current area
            # Area = width * min_height
            current_width = right - left
            current_height = min(height[left], height[right])
            current_area = current_width * current_height
            
            # Update max_area if the current container holds more water
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter line inward.
            # Why? Because the width is decreasing. To possibly get a larger area,
            # we need a taller line, which can only be found by moving the shorter one.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area