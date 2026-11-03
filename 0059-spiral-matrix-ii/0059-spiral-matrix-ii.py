class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        
        while top <= bottom and left <= right:
            # 1. Fill the top row (left to right)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # 2. Fill the right column (top to bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # 3. Fill the bottom row (right to left)
            # Check if top <= bottom to avoid overwriting in case of a single middle row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1
                
            # 4. Fill the left column (bottom to top)
            # Check if left <= right to avoid overwriting in case of a single middle column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1
                
        return matrix