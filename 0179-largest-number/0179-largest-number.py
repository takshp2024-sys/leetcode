from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator function
        def compare(a, b):
            # If a + b > b + a, then 'a' should come before 'b'
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
                
        # Convert all numbers to strings
        str_nums = [str(num) for num in nums]
        
        # Sort using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))
        
        # Join the sorted strings
        result = "".join(str_nums)
        
        # Edge case: if the result is all zeros (e.g., [0, 0]), return "0" instead of "00"
        if result[0] == '0':
            return "0"
            
        return result