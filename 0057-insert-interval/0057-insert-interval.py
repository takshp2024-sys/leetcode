class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        
        # Phase 1: Add all intervals that end strictly before the new interval starts.
        # They don't overlap and come before the new interval.
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
            
        # Phase 2: Merge all intervals that overlap with the new interval.
        # They overlap if the current interval starts before or at the same time 
        # the new interval ends.
        while i < n and intervals[i][0] <= newInterval[1]:
            # Update the new interval's start and end to cover the overlapping interval
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        # Add the merged new interval to the result
        result.append(newInterval)
        
        # Phase 3: Add all remaining intervals that come after the new interval.
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result