class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate the area of the first rectangle
        areaA = (ax2 - ax1) * (ay2 - ay1)
        
        # Calculate the area of the second rectangle
        areaB = (bx2 - bx1) * (by2 - by1)
        
        # Calculate the dimensions of the overlapping rectangle
        # The width of the overlap is the minimum of the right edges minus the maximum of the left edges
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        # The height of the overlap is the minimum of the top edges minus the maximum of the bottom edges
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        # If the width and height are both positive, there is a valid overlap
        if overlap_width > 0 and overlap_height > 0:
            overlap_area = overlap_width * overlap_height
        else:
            overlap_area = 0
            
        # Total area = Area A + Area B - Overlap Area
        return areaA + areaB - overlap_area