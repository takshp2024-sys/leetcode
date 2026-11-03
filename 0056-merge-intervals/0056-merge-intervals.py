class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If the merged list is empty, or if the current interval does not overlap with the last one
            # (i.e., the start of the current interval is strictly greater than the end of the last merged interval)
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is an overlap. We merge the intervals by updating the end time
                # to the maximum of the two end times.
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged