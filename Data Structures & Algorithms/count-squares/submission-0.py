from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.point_counts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        pt = tuple(point)
        self.point_counts[pt] += 1
        self.points.append(pt)

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total_squares = 0

        for x, y in self.points:
            if abs(qx - x) != abs(qy - y) or qx == x or qy == y:
                continue

            corner1 = (qx, y)
            corner2 = (x, qy)

            total_squares += self.point_counts[corner1] * self.point_counts[corner2]

        return total_squares
