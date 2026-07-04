class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        maxarea = 0
        for i in range(len(heights)):
            a = heights[i]
            left = i
            right = i
            while heights[left -1] >= a and left - 1 >= 0:
                left = left - 1
            while right + 1 < len(heights) and heights[right + 1] >= a:
                right = right + 1
            area = (right - left + 1) * a
            maxarea = max(area, maxarea)
        return maxarea