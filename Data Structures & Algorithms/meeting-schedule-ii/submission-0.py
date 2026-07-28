"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        rooms = []
        
        for interval in intervals:
            start =interval.start
            end = interval.end
            placed = False
            for i in range(len(rooms)):
                if rooms[i] <= start:
                    rooms[i] = end
                    placed = True
                    break
            if not placed:
                rooms.append(end)
        return len(rooms)