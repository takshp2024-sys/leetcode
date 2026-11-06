class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        # There are 2^n elements in the sequence
        for i in range(1 << n):
            # Generate the Gray code using the formula: i ^ (i >> 1)
            result.append(i ^ (i >> 1))
        return result