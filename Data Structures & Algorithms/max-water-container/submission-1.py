class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxval = 0
        val = 0
        for i in range (len(heights)):
            for j in range(i+1, len(heights)):
                val = (j - i)*(min(heights[i],heights[j]))
                maxval = max(val, maxval)
        return maxval