class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the array to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers upwards
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Update the maximum streak
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak