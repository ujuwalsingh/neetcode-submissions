class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        maxarea = 0
        for i in range(len(heights)):
            a = heights[i]
            left = i
            right = i
            arr = deque()
            while heights[left - 1] >= a and left - 1 >= 0:
                arr.appendleft(heights[i-1])
                left -= 1
            while right + 1 < len(heights) and heights[right + 1] >= a:
                arr.append(heights[i+1])
                right += 1
            area = (len(arr) + 1) * a
            maxarea = max(area, maxarea)
        return maxarea