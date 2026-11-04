class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        # Flags to check if the first row or first column needs to be zeroed
        first_row_zero = False
        first_col_zero = False
        
        # 1. Determine if the first row and first column need to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
                
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
                
        # 2. Use the first row and first column as markers for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 3. Zero out the cells based on the markers
        # We skip the first row and first column here because they are our markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 4. Zero out the first row and first column if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0