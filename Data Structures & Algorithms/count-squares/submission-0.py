class CountSquares:

    def __init__(self):
        self.points_count = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        p = tuple(point)
        if self.points_count[p] == 0:
            self.points.append(p)
        self.points_count[p] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total_squares = 0
        for x3, y3 in self.points:
            if (abs(x1-x3) != abs(y1-y3) or x1 == x3 or y1 == y3):
                continue
            
            p2 = (x1, y3)
            p4 = (x3, y1)

            total_squares += (
                self.points_count.get((x3,y3)) * self.points_count.get(p2,0) * self.points_count.get(p4, 0)
            )
        return total_squares
