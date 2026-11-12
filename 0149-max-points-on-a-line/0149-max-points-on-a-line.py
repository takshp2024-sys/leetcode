from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 0
        
        for i in range(n):
            # Dictionary to store the frequency of each slope starting from point i
            # Key: (dx, dy) as a reduced fraction, Value: count of points on this line
            slopes = defaultdict(int)
            
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # Reduce the fraction dy/dx by dividing by their GCD
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalize the sign so that (-1, 1) and (1, -1) are treated the same
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    # Vertical line
                    dy = 1
                elif dy == 0:
                    # Horizontal line
                    dx = 1
                    
                slopes[(dx, dy)] += 1
                
            # The maximum number of points on a line through point i is the max slope count + 1 (for point i itself)
            if slopes:
                max_points = max(max_points, max(slopes.values()) + 1)
            else:
                max_points = max(max_points, 1)
                
        return max_points