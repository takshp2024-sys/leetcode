class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        # We start with an even prefix sum (sum of 0 elements is 0, which is even)
        even_count = 1
        odd_count = 0
        
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 0:
                # If current prefix sum is even, it forms an odd sum with all previous odd prefix sums
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                # If current prefix sum is odd, it forms an odd sum with all previous even prefix sums
                result = (result + even_count) % MOD
                odd_count += 1
                
        return result