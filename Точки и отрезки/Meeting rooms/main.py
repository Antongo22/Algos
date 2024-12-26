from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        current_rooms = 0
        max_rooms = 0

        rooms = []
        for i in intervals:
            rooms.append([i.start, 1])
            rooms.append([i.end, -1])

        rooms.sort()

        for i in rooms:
            current_rooms += i[1]

            max_rooms = max(max_rooms, current_rooms)
        return max_rooms

