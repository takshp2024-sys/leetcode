class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        MAX_POW_3 = 1162261467  # 3^19, largest power of 3 within 32-bit signed int
        return n > 0 and MAX_POW_3 % n == 0