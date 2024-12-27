from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passengers = []

        for trip in trips:
            passengers.append([trip[1], trip[0]])
            passengers.append([trip[2], trip[0] * -1])

        passengers.sort()

        for i in passengers:
            capacity -= i[1]

            if capacity < 0:
                return False

        return True