class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        a = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                a.append(interval)
            elif interval[0] > newInterval[1]:
                a.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        a.append(newInterval)
        return a
        