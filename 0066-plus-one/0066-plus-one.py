class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate from the end of the array to the beginning
        for i in range(len(digits) - 1, -1, -1):
            # If the current digit is less than 9, we can simply add 1 and we are done
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and the carry propagates to the next left digit
            digits[i] = 0
            
        # If we finish the loop, it means all digits were 9 (e.g., 999 -> 000)
        # We need to add a new leading 1
        return [1] + digits