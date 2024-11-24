from typing import (
    List,
)

class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """
    def is_reflected(self, points: List[List[int]]) -> bool:
        
        maxX = -2_147_483_648
        minX = 2_147_483_647
        
        for point in points:
            maxX = max(maxX, point[0])
            minX = min(minX, point[0])

        pointsSet = set((x, y) for x, y in points)

        for x, y in pointsSet:
            if (maxX + minX - x, y) not in pointsSet:
                 return False
        return True