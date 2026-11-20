class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the most recent index of each number
        last_seen = {}
        
        for i, num in enumerate(nums):
            # If the number is in the dictionary and the distance is <= k
            if num in last_seen and i - last_seen[num] <= k:
                return True
                
            # Update the most recent index of the number
            last_seen[num] = i
            
        return False