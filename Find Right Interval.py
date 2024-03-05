class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for index, interval in enumerate(intervals):
            interval.append(index)
        intervals.sort()
        n = len(intervals)
        answer = [-1] * n  # Initialize the answer list with -1
        for _, end, o_index in intervals:
            r_index = bisect_left(intervals, [end])
            if r_index < n:
                answer[o_index] = intervals[r_index][2]
      
        return answer 
