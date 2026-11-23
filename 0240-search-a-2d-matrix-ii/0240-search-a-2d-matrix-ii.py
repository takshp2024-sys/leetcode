class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        
        # Start from the top-right corner
        row = 0
        col = n - 1
        
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # The current element is too large, eliminate this column
                col -= 1
            else:
                # The current element is too small, eliminate this row
                row += 1
                
        return False