class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def is_valid(start: int, num1: str, num2: str) -> bool:
            # Must consume the entire string and produce at least a third number
            if start == n:
                return False

            while start < n:
                total = str(int(num1) + int(num2))
                if not num.startswith(total, start):
                    return False
                start += len(total)
                num1, num2 = num2, total

            return True

        # First number ends at index i (length i + 1)
        for i in range(1, n - 1):
            if num[0] == "0" and i > 1:
                break
            num1 = num[:i]

            # Second number spans [i, j) (length j - i)
            for j in range(i + 1, n):
                if num[i] == "0" and j - i > 1:
                    break
                # Need at least 1 digit left for the third number
                if n - j < max(len(num1), j - i):
                    break

                num2 = num[i:j]
                if is_valid(j, num1, num2):
                    return True

        return False