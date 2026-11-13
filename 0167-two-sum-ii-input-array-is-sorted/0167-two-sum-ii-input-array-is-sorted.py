class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-based indices
                return [left + 1, right + 1]
            elif current_sum < target:
                # We need a larger sum, so move the left pointer right
                left += 1
            else:
                # We need a smaller sum, so move the right pointer left
                right -= 1
                
        return [] # Unreachable given the problem guarantees a solution