class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 (except 0 itself) are not palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # We only need to reverse half of the number.
        # When the reversed half becomes greater than or equal to the remaining x,
        # we have reached the middle of the number.
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # For even length numbers, x == reversed_half.
        # For odd length numbers, the middle digit doesn't matter, so we divide reversed_half by 10.
        return x == reversed_half or x == reversed_half // 10