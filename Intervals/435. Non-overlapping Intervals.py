# https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75

# Case 1: Non-overlapping intervals
    # No need to remove any interval
# Case 2: Completely overlapping intervals
    # Remove larger interval
# Case 3: Partially overlapping intervals
    # Remove one of the intervals, or both



# Approach 1: Greedy
# Sort the intervals by their end time
# Iterate through the intervals, and remove the interval with the larger end time
# Time complexity: O(nlogn)


class Solution(object):
    # Keep track of non-overlapping intervals
    def eraseOverlapIntervalsPointer(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        keep = [intervals[0]]

        for interval in intervals: 
            if keep[-1][1] <= interval[0]:
                keep.append(interval)
        
        return len(intervals) - len(keep)

    # Pointer approach
    def eraseOverlapIntervalsPointer(self, intervals):    
        intervals.sort(key=lambda x: x[1])      
        left, right = 0, 1
        count = 0

        while right < len(intervals):
            # Overlap, delete right interval
            if intervals[left][1] > intervals[right][0]:        
                count += 1
                right += 1
            else:
                left = right
                right += 1
        
        return count
