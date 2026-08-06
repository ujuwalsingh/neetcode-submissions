class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = []
        for interval in intervals:
            if not arr or arr[-1][1] < interval[0]:
                arr.append(interval)
            else:
                arr[-1][1] = max(arr[-1][1],interval[1])
        return arr