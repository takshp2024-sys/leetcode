class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_sum = 0
            for c in range(n):
                row_sum += matrix[r][c]
                self.dp[r + 1][c + 1] = self.dp[r][c + 1] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)