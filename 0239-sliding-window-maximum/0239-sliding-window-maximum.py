from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # Stores indices, values are in decreasing order
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Maintain the monotonic property: remove elements smaller than the current
            # They can never be the maximum as long as 'num' is in the window
            while dq and nums[dq[-1]] < num:
                dq.pop()
                
            # 3. Add the current element's index
            dq.append(i)
            
            # 4. Record the maximum for the window once we have processed at least 'k' elements
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result