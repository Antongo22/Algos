class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_start = 0
        pointer_end = len(height) - 1

        max_area = 0

        while pointer_start < pointer_end:
            max_area = max(max_area, min(height[pointer_start], height[pointer_end]) * (pointer_end - pointer_start))
            if height[pointer_start] < height[pointer_end]:
                pointer_start += 1
            else:
                pointer_end -= 1

        return max_area
